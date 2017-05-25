#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

d = {1: (2, [3, 4], 5, 6), 7: 8}

print(d[1][-1:]) # Rückwärts Tupel bei 1: Slice von letztes bis letztes (6,)
print(d[1][1][:1]) # Tupel bei 1 davon das 2. Element von Anfang bis 1 exklusive (ende) Slice -> [3]
print(d.items()) # alles aus dem Dic Tupel (key, Value)
