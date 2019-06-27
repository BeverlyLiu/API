import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read Input Json File
with open("C:\\Users\\beile\\PycharmProjects\\APIAutomation\\CreateUser.json", 'r') as file:
    json_input = file.read()
    request_json = json.loads(json_input)

# Make POST request with Json Input body
response = requests.post(url, request_json)
#print(response.content)
#print(response)
assert response.status_code == 201

# Fetch Header from Response
print(response.headers)
print(response.headers.get("Content-Length"))

# Parse response to Json Format
response_json = json.loads(response.text)

# Pick ID using Json Path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])
