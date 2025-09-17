import os

print(os.name)     #Output : posix (on Unix-like systems), nt (on Windows)
print(os.getcwd()) #Output : Current working directory
os.mkdir("new_directory") #Create a new directory