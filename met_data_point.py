import requests
import json
from met_app_key import app_key

APP_KEY = app_key()
BASE = 'http://datapoint.metoffice.gov.uk/public/data/'
RESOURCE = 'val/wxobs/all/json/sitelist'
URL = BASE + RESOURCE + '?key=' + APP_KEY

#response = requests.get("http://api.open-notify.org/iss-now.json")
#URL =\
#'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/3840?res=3hourly&key='\
#+ APP_KEY
#print(URL)
#response = requests.get(URL)

# Print the status code of the response.
#print(response.status_code)
#content = response.json()
#content = content['Locations']['Location']
#print(content)
#for item in content:
#    try:
#        if 'ondon' in item['unitaryAuthArea']:
#            print(item)
#    except:
#        pass

LOCATION_ID = 3772 #Heathrow
RESOURCE = 'val/wxobs/all/json/3772'
#RESOURCE = 'val/wxfcs/all/json/3840'
URL = BASE + RESOURCE + '?res=hourly&key=' + APP_KEY
response = requests.get(URL)
content = response.json()
content_key = content['SiteRep']['Wx']['Param']
for item in content_key:
    print(item)

content = content['SiteRep']['DV']['Location']['Period']
for item in content:
    for hour in item['Rep']:
        print(hour)
#print(content)
