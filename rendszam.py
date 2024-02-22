def legujabb_rendszam(rendszam):
    if len(rendszam) == 9:
        if rendszam[2] == '-' and rendszam[5] == '-':
            if rendszam[:2].isupper() and rendszam[4:5].isupper() and rendszam[6:].isdigit():
                return True
    return False

def ellenoriz_uj_rendszam(rendszam):
    # Ellenőrizze, hogy az új típusú rendszám formátuma helyes-e
    if len(rendszam) == 8:
        if rendszam[4] == '-':
            if rendszam[:4].isupper() and rendszam[5:].isdigit():
                return True
    return False

def ellenoriz_regi_rendszam(rendszam):
    # Ellenőrizze, hogy a régi típusú rendszám formátuma helyes-e
    if len(rendszam) == 7:
        if rendszam[3] == '-':
            if rendszam[:3].isupper() and rendszam[4:].isdigit():
                return True
    return False

def rendszam_formatum(rendszam):
    for karakter in rendszam:
        if not (karakter.isalnum() or karakter == '-'):
            return "Nem megfelelő karakterek vannak a rendszámban."
    if legujabb_rendszam(rendszam):
        return f"A(z) {rendszam} rendszám a a legújabb típusú"
    elif ellenoriz_uj_rendszam(rendszam):
        return f"A(z) {rendszam} rendszám új típusú."
    elif ellenoriz_regi_rendszam(rendszam):
        return f"A(z) {rendszam} rendszám régi típusú."
    else:
        return "Nem sikerült azonosítani a rendszám típusát. Kezdd előről az adatbevitelt!" 




       
#i = 1
while True:
    rendszam = input("Kérem, adja meg a rendszámot: ")
    eredmeny = rendszam_formatum(rendszam)
    print(eredmeny)            
    #rendsz = open('rendszamok.txt', 'a', encoding='UTF-8')
    #rendsz.write(eredmeny)
    #rendsz.write(' Sorszám:')
    #rendsz.write(str(i))
    #i += 1
    #rendsz.write(" \n")
    #rendsz.close()