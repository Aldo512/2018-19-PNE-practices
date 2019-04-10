import requests

data = requests.get('http://www.ensembl.org/index.html')

gene = 'FRAT1'
j = requests.post(('http://www.ensembl.org/Multi/Search/Results?q=FRAT1;site=ensembl'))

k = requests.get('http://www.ensembl.org/Multi/Search/Results?q=FRAT1;site=ensembl')