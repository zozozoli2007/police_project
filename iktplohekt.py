'''def rendszam_e(rendsz):
    itelet = 0
    return itelet'''

rsze = input("Mi a rendszám\n")
'''a = rendszam_e(rsze)

if (a == 0):
    print('Nem rendszám!')
elif (a == 1):
    print('Régi rendszám.')
else:
    print('Új rendszám.')'''


li = list(rsze)
betu=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if li[5] == '-':
    print("Műkszik")
    if li[2] == "-":
        print("Műkszik")
        
elif li[4]=="-":
    print("Műkszik")
else:
    print("nem jo")