# -- Example of a client that uses the HTTP.client library
# -- for requesting a JSON object and printing their
# -- contents
import http.client
import json
import termcolor

SERVER = 'http://www.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000165879;r=10:97319267-97321915'

print("\nConnecting to server: {}\n".format(SERVER))

page = http.client.HTTPConnection(SERVER, 80)

print(page)
