import json
import jsonpath
import requests

def test_add_new_data():
    App_URL = "http://thetestingworldapi.com/api/studentsDetails"
    with open("C:\\Users\\beile\\PycharmProjects\\APIAutomation\\studentsDetail.json", 'r') as file:
        request_json = json.loads(file.read())
        response = requests.post(App_URL, request_json)
        print("App Response text: ", response.text)
        id = jsonpath.jsonpath(response.json(), "id")
        print("id: ", id[0])

    Tech_API_URL = "http://thetestingworldapi.com/api/technicalskills"
    with open("C:\\Users\\beile\\PycharmProjects\\APIAutomation\\techDetail.json", 'r') as tech_file:
        request_json = json.loads(tech_file.read())
        request_json['id'] = int(id[0])
        request_json["st_id"] = id[0]
        response = requests.post(Tech_API_URL, request_json)
        print("Tech response text: ", response.text)

    Address_API_URL = "http://thetestingworldapi.com/api/addresses"
    with open("C:\\Users\\beile\\PycharmProjects\\APIAutomation\\addressDetail.json", 'r') as address_file:
        request_json = json.loads(address_file.read())
        request_json['stId'] = id[0]
        response = requests.post(Address_API_URL, request_json)

        final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
        response = requests.get(final_details)
        print("address response text: ", response.text)