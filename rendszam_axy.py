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
                if li[1].upper() in betu:
                    if li[3].upper() in betu:
                        if li[4].upper() in betu:
                            if li[6].upper() in szam:
                                if li[7].upper() in szam:
                                    if li[8].upper() in szam:
                                        return 1
                            else:
                                return 0
                        else:
                            return 0
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
    #Itt pedig ellenőriztük hogy "AAAA-111" formátumban van-e
    elif li[4]=="-":
        if li[0].upper() in betu:
            if li[1].upper() in betu:
                if li[2].upper() in betu:
                    if li[3].upper() in betu:
                        if li[5].upper() in szam:
                            if li[6].upper() in szam:
                                if li[7].upper() in szam:
                                    return 2
                            else:
                                return 0
                        else:
                            return 0
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    #Itt ellenőrzöm hogy régi rendszám-e
    elif li[3]=="-":
        if li[0].upper in betu:
            if li[1].upper in betu:
                if li[2].upper in betu:
                    if li[4] in szam:
                        if li[5] in szam:
                            if li[6] in szam:
                                return 3
                        else:
                            return 0
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0
        
#Itt kezdődik egy teszt program
while True:
    rsze = input("Mi a rendszám\n")

    li = list(rsze)

    #Meghívjuk az alprogramot

    answer=(rendszam(li))

    #Itt pedig kiadjuk a választ
    
    if (answer==1):
        print("A rendszám új")
        break
    elif (answer==2):
        print("A rendszám új")
        break
    else:
        print("Az ellenőrzés alatt hiba lépett fel. Kérem ismételje meg a bevitelt\n")
