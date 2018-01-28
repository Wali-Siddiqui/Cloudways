import requests
import json

API_KEY = "xxxxxxxx"
EMAIL = "xxxxxx"
SERVER_ID = 'xxxxx'
BASE_URL = "https://api.cloudways.com/api/v1/oauth/access_token"
Service = 'xxxxxx'

#'apache2'  'memcached' 'mysql 'php7.0-fpm' 'php5-fpm'  'nginx' 'varnish'


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
  
def service_restart(token,SERVER_ID,Service):
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'Authorization': 'Bearer '+token+'',
     }

    data = [('server_id', SERVER_ID),('service', Service),('state', 'restart'),]

    response = requests.post('https://api.cloudways.com/api/v1/service/state', headers=headers, data=data)

    return (response)

def main ():
    token = access_token(API_KEY,EMAIL,BASE_URL)
    print ('Access Token has been generated :'+str(token))
    
    varnish = service_restart(token,SERVER_ID,Service).status_code
    if varnish == int(varnish) and str(token) != 'None':
       print(Service + "has been restarted")
    else:
       print ("Unexpected Error")
   
if __name__ == "__main__":
    main() 



