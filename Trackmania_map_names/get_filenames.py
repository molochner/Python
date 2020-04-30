import os

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

file1 = open("TMServer/maplist.txt", "w")

for file in files("TMServer/maps"):
    file1.write("<map><file>Downloaded/" + file + "</file></map>\n")
    #print ("<map><file>Downloaded/" + file + "</file></map>")

file1.close()