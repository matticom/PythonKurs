#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import re
zeichenk = "uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh"
muster = ("uu*?", "[1-9]+", ".+:.+?:", "[ucp]+?", "s[sh]*?", "(?<=/).+?")
for item in muster:
    print(item, " = ", re.search(item, zeichenk).group())
# "uu*?"       nicht gierig, alles
# "[1-9]+"    1
# ".+:.+?:"   nicht gierig, uucp:... (bis letztes ':')
# "[ucp]+?"   nicht gierig, u
# "s[sh]*?"   nicht gierig, sh
# "(?<=/).+?"  nicht gierig, positive lookbehind assertion, sucht Übereinstimmung mit '/'