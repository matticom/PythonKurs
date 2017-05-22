#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import re
print(re.search('bert','Albert').group())
print(re.search('\$','$').group())  # $ = Ende der Zeile/Wort (mit Maskierung nur "$")
print(re.search('\$$','$').group()) # Sucht $ am Ende des Wortes
print(re.search('^[^^]','X^X').group()) # ^= am Anfang des Wortes/Zeile [^...] = negiert -> Suchen alle Zeichen außer ^ am Anfang
print(re.search('[abc]+','xxxaaaddd').group()) # += eins von den Zeichen in [] 1 oder mehrmals 
print(re.search('[abc]','xxxaaaddd').group()) # eins von den Zeichen
