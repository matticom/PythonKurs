import os
#print([datei for datei in os.listdir('.') if 3 <= len(datei) < 6])
for datei in os.listdir('.'):
    if 3 <= len(datei) < 20:
        print(datei)
