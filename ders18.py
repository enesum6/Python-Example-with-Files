
import os

file="C:\\Users\\PC\\OneDrive\\MasaÜstü\\deneme3.txt"
filename=open(file,"r+")
text=filename.readlines()
for i in text:
    filename.write("ogrencilerin ortalaması:len(text)/ortalama")
