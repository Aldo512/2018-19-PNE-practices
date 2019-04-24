import http.client
import json

HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query="
METHOD = "GET"

conn = http.client.HTTPSConnection(HOSTNAME)

usrct = input('Which city do you want to know the forecast from?: ')
conn.request(METHOD, ENDPOINT + usrct)
ans = conn.getresponse()
text_json = ans.read().decode("utf-8")
conn.close()
weather = json.loads(text_json)


print(weather)
print(weather[0]['woeid'])