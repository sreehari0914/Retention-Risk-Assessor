// src/App.js
import React from 'react';
import FileUpload from './components/FileUpload';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>XLSX File Editor</h1>
            </header>
            <FileUpload />
        </div>
    );
}

export default App;
