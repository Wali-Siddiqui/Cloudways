import requests
import json

API_KEY = "xxxx"
EMAIL = "xxxxx"
SERVER_ID = xxxxx
BASE_URL = "https://api.cloudways.com/api/v1/oauth/access_token"
Application = 'WordPress'
app_version = '4.9.4'
project_name = 'xxxxxx'
application_name = 'xxxxx'

def access_token(API_KEY,EMAIL,BASE_URL):
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',}
    data = [
    ('email', EMAIL),
    ('api_key', API_KEY),]
    token = requests.post('https://api.cloudways.com/api/v1/oauth/access_token', headers=headers, data=data)
    value = json.loads(token.text).get('access_token')
    return (value)


def add_applicaton(token,SERVER_ID,Application,app_version,application_name,project_name):
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'Authorization': 'Bearer '+token+'',
     }

    data = [('server_id', SERVER_ID),('application',Application),('app_version', app_version), ('app_label', application_name),('project_name', project_name)]

    response = requests.post('https://api.cloudways.com/api/v1/app', headers=headers, data=data)

    return (response.text)

def main ():
    token = access_token(API_KEY,EMAIL,BASE_URL)
    print ('Access Token has been generated :'+str(token))
    add_application = str(add_applicaton(token,SERVER_ID,Application,app_version,application_name,project_name))
    print(add_application)
    
if __name__ == "__main__":
    main() 
