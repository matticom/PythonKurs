#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, pickle
dic={}
path="C:\\Users\\Matti\\txt_examples"
try:
    loadedModul=open(os.path.join(path, "pyDict"), 'rb')
    dic = pickle.load(loadedModul)
    loadedModul.close
except FileNotFoundError:
    print("\nDas Wörterbuch ist noch nicht vorhanden und wird jetzt angelegt\n\n")
files = [file for file in os.listdir(path) if file[-4:] == '.txt']
for file in files:
    fullPath=os.path.join(path, file)
    f=open(fullPath, 'r')
    wordStr = f.read()
    f.close
    words = wordStr.split()
    for word in words:
        if word not in dic:
            dic[word] = [file,]
        elif file not in dic[word]:
            dic[word].append(file)
    for x in dic.items():
        print(x)
    print("\n\n")
##  rueckgabeList = map(lambda x: print(x), dic.items())
    modul=open(os.path.join(path, "pyDict"), 'wb')
    pickle.dump(dic, modul)
    modul.close
