#Alprogram ami az új rendszám fajtát ismeri fel

def rendszam(rsze):
    #Egy-egy tuple belsejében elhelyeztük a betüket és számokat
    betu=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    szam=("0","1","2","3","4","5","6","7","8","9")
    #Ellenőriztük hogy a rendszám "AA-AA-111" formátumban van-e
    if li[5] == '-':
        if li[2] == "-":
            #Ellenőriztük hogy 1-2-ig és 4-5-ig betük vannak-e
            if li[0].upper() in betu:
                print("Jo")
            if li[1].upper() in betu:
                print("Jo")
            if li[3].upper() in betu:
                print("jo")
            if li[4].upper() in betu:
                print("Jo")
            if li[6].upper() in szam:
                print("jo")
            if li[7].upper() in szam:
                print("jo")
            if li[8].upper() in szam:
                print("jo")
            else:
                print("nem jo")
    #Itt pedig ellenőriztük hogy "AAAA-111" formátumban van-e
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
    return
        
#Itt kezdődik egy teszt program

rsze = input("Mi a rendszám\n")

li = list(rsze)

#Meghívjuk az alprogramot
rendszam(li)
