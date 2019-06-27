import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users/2"

# Read Input Json File
with open("C:\\Users\\beile\\PycharmProjects\\APIAutomation\\CreateUser.json", 'r') as file:
    json_input = file.read()
    request_json = json.loads(json_input)

# Make PuT request with Json Input body
response = requests.put(url, request_json)

# Validating Response Code
assert response.status_code == 200

# Parse response Content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, "updatedAt")
print(updated_li[0])
