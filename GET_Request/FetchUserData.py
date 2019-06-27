import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
# print(response)

# Display Response Content
# print(response.content)
# print(response.headers)

# Parse response to Json format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using Json Path
page = jsonpath.jsonpath(json_response, 'per_page')
pages = jsonpath.jsonpath(json_response, 'total_pages')

assert pages[0] == 4
