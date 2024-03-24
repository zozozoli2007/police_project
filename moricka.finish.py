#Alprogram

def rendszam_e(rsz):
    if rsz[3]=="-":
        if rsz[:3].isupper() and rsz[4:].isdigit():
            return 1
        else:
            return 0
    elif rsz[2]=="-" and rsz[5]=="-":
        if rsz[:2].isupper() and rsz[3:4].isupper() and rsz[6:].isdigit():
            return 2
        else:
            return 0
    elif rsz[4]=="-":
        if rsz[:4].isupper() and rsz[5:].isdigit():
            return 2
        else:
            return 0
    else:
        return 0

#Főprogram amit már elkészítettek nekünk.

'''rsze = input('Rendszám: ')

a = rendszam_e(rsze)
print(a)
if (a == 0):
    print('Nem rendszám!')
elif (a == 1):
    print('Régi rendszám.')
else:
    print('Új rendszám.')'''