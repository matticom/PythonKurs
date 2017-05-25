import os
#print([datei for datei in os.listdir('.') if 3 <= len(datei) < 6 and os.path.isfile(datei)])
#print(list(filter(lambda datei: 3 <= len(datei) < 6  and os.path.isfile(datei), os.listdir('.'))))
for datei in os.listdir('.'):
    if 3 <= len(datei) < 20:
        print(datei)
