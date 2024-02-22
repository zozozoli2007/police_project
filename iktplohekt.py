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
szam=["0","1","2","3","4","5","6","7","8","9"]

if li[5] == '-':
    if li[2] == "-":
        if li[0].upper() in betu:
            print("This")
        if li[1].upper() in betu:
            print("is")
        if li[3].upper() in betu:
            print("a")
        if li[4].upper() in betu:
            print("bucket")
        if li[6].upper() in szam:
            print("Dear,")
        if li[7].upper() in szam:
            print("god")
        if li[8].upper() in szam:
            print("There's more")
        else:
            print("nem jo")
elif li[4]=="-":
    print("Műkszik")
    if li[0].upper() in betu:
        print("Red")
    if li[1].upper() in betu:
        print("spy")
    if li[2].upper() in betu:
        print("is")
    if li[3].upper() in betu:
        print("based")
    if li[5].upper() in szam:
        print("Based?")
    if li[6].upper() in szam:
        print("Based on what?")
    if li[7].upper() in szam:
        print("Sex")
    else:
        print("nem jo")
else:
    print("nem jo")