import http.client
import json

HOSTNAME = "api.icndb.com"
ENDPOINT = ["/jokes/random", "/jokes/count", "/categories"]
METHOD = "GET"


headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

commands =['Joke: ', 'The total number of jokes in the database is: ', "joke categories: "]

for end in ENDPOINT:
    conn.request(METHOD, end)
    r1 = conn.getresponse()
    text_json = r1.read().decode("utf-8")
    conn.close()
    chuck = json.loads(text_json)
    if end == "/jokes/random":
        print()
        print(commands[0] + chuck['value']['joke'])
    elif end == "/jokes/count":
        print()
        print(commands[1] + str(chuck['value']))
    elif end == "/categories":
        print()
        print('The categories for the jokes are:')
        for cats in chuck['value']:
            print(cats)
