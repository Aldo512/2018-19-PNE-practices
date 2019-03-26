import re

def allowed_char(string):
    charRe = re.compile(r'[^ACTG-actg.]')
    string = charRe.search(string)
    return not bool(string)

test = 'actz'
print(allowed_char(test))
