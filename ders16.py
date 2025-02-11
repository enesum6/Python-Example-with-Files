import os

file_path="C:\\Users\\PC\\OneDrive\\Masaüstü\\Try"
with open(file_path,"w") as dosyam:
    num=10
    alpha=["Ali,Veli"]
    dosyam.write("Merhaba Dünyalı\n")
    dosyam.write("Hello World\n"+str(num))
    dosyam.write("Hello"+str(alpha))