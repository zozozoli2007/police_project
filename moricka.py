# "Móricka" főprogram, csak arra jó, hogy meghívja a függvényünket
# és kezelje az általunk visszaadott eredményeket.

def rendszam_e(rendsz):
    itelet = 0
    return itelet

rsze = input('Rendszám: ')

a = rendszam_e(rsze)

if (a == 0):
    print('Nem rendszám!')
elif (a == 1):
    print('Régi rendszám.')
else:
    print('Új rendszám.')