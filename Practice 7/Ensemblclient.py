import requests, sys

server = "http://rest.ensembl.org"
ext = "/sequence/id/GENSCAN00000000001?type=protein;object_type=predictiontranscript;db_type=core;species=homo_sapiens"

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
filein = repr(decoded)

done = filein.split(',')
writing = open('Jsontest.json', 'w')

for info in range(len(done)):

    if info < len(done)-1:
        writing.write(done[info].replace("'", '"') + ',' + '\n')

    elif info == len(done)-1:
        writing.write(done[info].replace("'", '"'))

writing.close()
print(len(decoded['seq']))
print(sys.path)