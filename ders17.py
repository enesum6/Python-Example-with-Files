import os
file="C:\\PC\OneDrive\\Masaüstü\\Try.txt"

try:
    dosyam=open(file,"r")
except:
    print("there is a error")
else:
    print("file is opened")
    