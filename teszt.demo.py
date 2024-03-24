# Rendszám függvények

import re

def rendszam_u1(rendszam_uj1):
    # A rendszám tábla formája: AAAA-111
    karakter = r'^[A-Z]{4}-[0-9]{3}$'
    if re.match(karakter, rendszam_uj1):
        return True
    else:
        return False

def rendszam_u2(rendszam_uj2):
    # A rendszám tábla formája: AA-AA-111
    karakter = r'^[A-Z]{2}-[A-Z]{2}-[0-9]{3}$'
    if re.match(karakter, rendszam_uj2):
        return True
    else:
        return False

def rendszam_r(rendszam_regi):
    # A rendszám tábla formája: AAA-111
    karakter = r'^[A-Z]{3}-[0-9]{3}$'
    if re.match(karakter, rendszam_regi):
        return True
    else:
        return False



# Főprogram

def rendszam_e(rendsz):
    itelet = 0
    return itelet


rendsz = input('Kérem írja be a mezőbe a rendszámot: ')

a = rendszam_e(rendsz)

if (a == 0):
    print('Nem rendszámot írt be!')
elif (a == 1):
    print('A rendszám fajtája új típusú!')
else:
    print('A rendszám fajtája régi típusú!')