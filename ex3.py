import requests
import json

#url = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
#response = requests.get(url)

#content = response.content.decode('utf-8')
#parsed_content = json.loads(content)

#print( type(response), "\n", type(response.content), type(parsed_content))

station_id = 877
url = f'https://api.gios.gov.pl/pjp-api/rest/station/sensors/877'
response = requests.get(url)

if response.status_code != 200:
    exit()

stations = json.loads(response.content.decode("utf-8"))

print(stations)