import json
import termcolor

# -- Open the json file
f = open("person.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person = json.load(f)

phone = person["phoneNumber"]
name = []
for people in range(len(person["Firstname"])):
    name.append(person["Firstname"][people] + " " + person["Lastname"][people])
age = person["age"]
cprint = termcolor.cprint

print('Number of people in the library: ' + str(len(name)))

for names in range(len(name)):

    cprint("Name:", 'yellow')
    cprint(name[names], 'red')
    cprint(' ' + 'Age: ' + str(age[names]), 'cyan')

    for types in range(len(phone[names])):

        cprint('  ' + 'Phone: ' + phone[names][types]['type'], 'blue')
        cprint('    ' + phone[names][types]["number"], 'green')
