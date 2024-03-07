#Alprogram

def rendszam_e(rsz):
    betu=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    szam=("0","1","2","3","4","5","6","7","8","9")
    

#Főprogram

rsze = input('Rendszám: ')

a = rendszam_e(rsze)
print(a)
if (a == 1):
    print('Régi rendszám.')
elif (a == 2):
    print('Új rendszám.')
else:
    print('Nem rendszám!')