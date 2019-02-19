FILENAME = "mynotes.txt"

# -- Open the file for reading
f = open(FILENAME, 'r')

# -- Read the content of the file
contents = f.read()

# -- Print the contents
print("File: {}".format(f.name))
print("{}".format(contents))

# -- Closing the file
f.close()

# -- Open again for adding
f = open(FILENAME, "a")

# -- write some information to the file
f.write("WAT WAT WAT")

f.close()

print("End")