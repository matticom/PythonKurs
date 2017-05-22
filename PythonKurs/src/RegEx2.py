import re
zeichenk = "-rw-r--r-- 1 2 root root 1761 2012-02-13 22:53 passwd"
mu = ("[wr-]+?", # - -> nicht gierig sonst -rw-r--r--
      "[toad]+", # oot -> gierig
      "o+o", # oo
      "-+-", # --
      "2*2", # 2
      "2+0*1??" # 2 -> 1? ja/nein , nicht gierig -> die erste Bedingung reicht schon: 2+
      )
for item in mu:
    print(item, ":", re.search(item, zeichenk).group())

