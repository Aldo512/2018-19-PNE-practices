# Example for reading a file located in our local filesystem

# -- Filename to read
NAME = "mynotes.txt"

# -- Open the file
myfile = open(NAME, 'r')

# -- myfile is an object!!! Let's see what it has inside

# -- Print the filename
print("Print: file opened: {}".format(myfile.name))

# -- Read the whole file into a string
contents = myfile.read()

# -- Print the files's contents
print("The file contents are: {}".format(contents))
print("The end!")

# -- Close the file
myfile.close()