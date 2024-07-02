import requests

url = 'http://127.0.0.1:5000/predict'
files = {'file': open('C:/Users/domin/Downloads/HRanalysis.xlsx', 'rb')}
response = requests.post(url, files=files)

# Save the returned file
with open('predictions.xlsx', 'wb') as f:
    f.write(response.content)
