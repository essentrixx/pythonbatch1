import sys
print(sys.path)

import os
print(os.getcwd())
print(os.listdir())
print(os.__file__)

os.chdir("")
os.mkdir("")
os.makedirs("") # many folders and file
os.rmdir("")
os.rename("", "")

            # (str, list, list)
os.walk("currentdirpath", "dirnames", "filenames")   #  tree directory, tuple unpacking

os.environ.get("key")   # echo $USER, $PATH, in terminal
os.environ.get("TMP")

# path
print(os.path.join("", ""))