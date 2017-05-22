#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, pickle
dic={}
path=".\\txt_examples"
print(os.path.join(path, "useradressen.txt"))
try:
    file = open("useradressen.txt", "rb") 
    print(file.read()) 
    loadedModul=open("useradressen.txt", 'rb')
    dic = pickle.load(loadedModul)
    loadedModul.close
except FileNotFoundError:
    print("Adressdatei ist nicht vorhanden")

