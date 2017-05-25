#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import re
dic={}

# https://docs.python.org/3/library/re.html
def seperateLine(line): 
    "Wandelt line in eine Liste mit der PLZ und ein Tupel mit Name"
    csv = re.split(",", line)
    plz = re.split("\W+", csv[2])[-1]
    name = re.split("\W+", csv[0])
    nachname = name[-1]
    vorname = ""
    for part in name[:-1]:
        vorname = vorname + part + " "
    vorname = vorname[:-1]
    return [plz, (nachname, vorname)]

try:
    content = open("useradressen.txt")
    lines = content.read().splitlines()
    content.close
except FileNotFoundError:
    print("Adressdatei ist nicht vorhanden")
    
for line in lines:
    datensatz = seperateLine(line)
    plz = datensatz[0]
    name = datensatz[1]
    if plz not in dic:
            dic[plz] = [name]
    else:
        dic[plz].append(name)
print(dic)


