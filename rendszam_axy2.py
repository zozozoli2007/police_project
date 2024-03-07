#Alprogram

def rendszam_e(rsze):
    betu=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    szam=("0","1","2","3","4","5","6","7","8","9")
    if rsze[3]=="-":
        if rsze[:3] in betu and rsze[4:] in szam:
            return 1
    else:
        return 0
    return

#Főprogram

rsze = input('Rendszám: ')

a = rendszam_e(rsze)

if (a == 0):
    print('Nem rendszám!')
elif (a == 1):
    print('Régi rendszám.')
else:
    print('Új rendszám.')