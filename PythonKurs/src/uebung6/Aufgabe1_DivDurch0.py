#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def dividiere(x, y): return (x/y)

tests = ((23, 69), (42, 0), ('Spam', 'Eggs'))
try:
    for a, b in tests:
        print(a, b)
        try:
            print(dividiere(a, b))
        finally:
            print("Versuchte zu dividieren.")
except ZeroDivisionError:
    print('Aber ich mag nicht durch Null teilen!')
print('\nBye.')

