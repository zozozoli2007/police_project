rsze = input("Mi a rendszám\n")

li = list(rsze)
betu=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
szam=("0","1","2","3","4","5","6","7","8","9")

def rendszam(rsze):
    if li[5] == '-':
        if li[2] == "-":
            if li[0].upper() in betu:
                print("Jo")
            if li[1].upper() in betu:
                print("jo")
            if li[3].upper() in betu:
                print("jo")
            if li[4].upper() in betu:
                print("jo")
            if li[6].upper() in szam:
                print("jo")
            if li[7].upper() in szam:
                print("jo")
            if li[8].upper() in szam:
                print("jo")
            else:
                print("nem jo")
    elif li[4]=="-":
        print("Műkszik")
        if li[0].upper() in betu:
            print("jo")
        if li[1].upper() in betu:
            print("jo")
        if li[2].upper() in betu:
            print("jo")
        if li[3].upper() in betu:
            print("jo")
        if li[5].upper() in szam:
            print("jo")
        if li[6].upper() in szam:
            print("jo")
        if li[7].upper() in szam:
            print("jo")
        else:
            print("nem jo")
    else:
        print("nem jo")