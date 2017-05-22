import sys
liste=sys.argv[1:]
liste.reverse()
print(liste)
for idx, element in enumerate(liste):
    print(idx,": ", element)
    # i++ gibt es nicht
    
