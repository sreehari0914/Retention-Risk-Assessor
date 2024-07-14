import React, { useState } from 'react';
import axios from 'axios';
import CircularProgress from '@mui/material/CircularProgress';

function UploadIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
      <polyline points="17 8 12 3 7 8" />
      <line x1="12" x2="12" y1="3" y2="15" />
    </svg>
  );
}

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      alert('Please select a file first.');
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        responseType: 'blob',
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'predictions.xlsx');
      document.body.appendChild(link);
      link.click();

      setError(null);
    } catch (error) {
      console.error('Error uploading file:', error);
      setError('Failed to process file.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gradient-to-br from-[#6366F1] to-[#EC4899]">
      <form className="bg-[#F9FAFB] p-8 rounded-2xl shadow-xl w-full max-w-md space-y-6" onSubmit={handleSubmit}>
        <div className="text-center space-y-3">
          <h2 className="text-3xl font-bold text-[#F9FAFB] bg-gradient-to-r from-[#6366F1] to-[#EC4899] bg-clip-text text-transparent">
            HRAnalysis
          </h2>
          <p className="text-[#9CA3AF] text-lg">Select a file to upload to our server.</p>
        </div>
        <div className="space-y-4">
          <label
            htmlFor="file"
            className="block font-medium text-[#F9FAFB] bg-gradient-to-r from-[#6366F1] to-[#EC4899] bg-clip-text text-transparent"
          >
            Choose a File
          </label>
          <div className="flex items-center gap-3">
            <div className="relative bg-[#E5E7EB] rounded-md px-4 py-2 flex-1">
              <input
                type="file"
                id="file"
                className="absolute inset-0 opacity-0 w-full h-full"
                onChange={handleFileChange}
              />
              <span className="truncate">{file ? file.name : 'No file chosen'}</span>
            </div>
            <button
              type="submit"
              className="flex items-center justify-center rounded-md px-6 py-2 text-[#F9FAFB] bg-gradient-to-r from-[#6366F1] to-[#EC4899] hover:bg-gradient-to-l"
              disabled={loading}
            >
              {loading ? (
                <CircularProgress size={20} thickness={5} color="inherit" />
              ) : (
                <>
                  <UploadIcon className="w-5 h-5 mr-2" />
                  Upload
                </>
              )}
            </button>
          </div>
        </div>
        {loading && <p className="text-[#6366F1]">Processing...</p>}
        {error && <p className="text-red-500">{error}</p>}
      </form>
    </div>
  );
};

export default FileUpload;
