
'''
#Lab_7.1
with open("ertekek.txt", "rt") as f:
    lista = []
    for sor in f:
       # print(sor.strip()) #Kiiratas
        lista.append(int(sor))

print(lista)

with open("szamozott.txt", "w") as f:
    for i in range(len(lista)):
        f.write(f"{i+1}. {lista[i]} \n")

print(f"Beolvasva: {len(lista)} szám az ertekek.txt fájlból.")
print(f"Kiírva: {len(lista)} sor a szamozott.txt fájlba.")
'''

'''
#Lab_7.3
with open("ertekek.txt", "rt") as f:

    paros = []
    paratlan = []
    lista = []

    for sor in f:
        lista.append(int(sor))

    for szam in lista:
        if szam % 2 == 0:
            paros.append(szam)
        else:
            paratlan.append(szam)

    print(paros)
    print(paratlan)

def kiir_fajlba (fajlnev, lista):
    with open (fajlnev, "wt") as f:
        sorok = []
        for szam in lista:
            sorok.append(str(szam)+"\n")
        f.writelines(sorok)

kiir_fajlba("parosok.txt",paros)
kiir_fajlba("paratlanok.txt", paratlan)

print(f"{'Páros:':<10} {len(paros)} db, összeg: {sum(paros)}")
print(f"{'Paratlan:':<10} {len(paratlan)} db, összeg: {sum(paratlan)}")
'''

'''
Lab_8.3
szamok = []
szavak = []

with open("bemenet.txt", "rt", encoding="utf-8") as f:
    for sor in f:
        elemek = sor.split(" ")
        for elem in elemek:
            try:
                szam = int(elem)
                szamok.append(szam)

            except ValueError:
                szavak.append(elem)

with open("szamok_ki.txt", "wt") as f:
    for szam in szamok:
        f.write(str(szam)+ "\n")

with open("szavak.txt", "wt") as f:
    for szo in szavak:
        f.write(szo + "\n")

szam_db = len(szamok)
szam_osszeg = sum(szamok)
szam_atlag = szam_osszeg / szam_db
szam_mini = min(szamok)
szam_maxi = max(szamok)
print(f"Számok : {szam_db} db, összeg: {szam_osszeg}, átlag: {szam_atlag} \n min: {szam_mini}, max: {szam_maxi}")

szavak_db = len(szavak)
szo_maxi = max(szavak, key = len) #Leghosszab szo
ossz_betu = 0
for szo in szavak:
    ossz_betu += len(szo)

szavak_atlag = ossz_betu / szavak_db

print(f"Szavak : {szavak_db} db, leghosszabb: {szo_maxi} ({len(szo_maxi)} betű) \n átlagos szóhossz: {szavak_atlag}")
'''

#Lab_8.4

ervenyes_pontok = []
hibas_pontok = []
ismetlodes = 0
hossz = 0
erv_db = 0

with open("pontszamok.txt", "rt") as f:
    for sor in f:
        hossz += 1
        try:
            pont = int(sor)
            if pont <= 100 and pont >= 0:
                erv_db += 1
                if pont not in ervenyes_pontok:
                    ervenyes_pontok.append(pont)
                else:
                    ismetlodes += 1
            else:
                hibas_pontok.append(sor)
        except ValueError:
            hibas_pontok.append(sor)

# print(f"{erv_db}")
# print(f"{ervenyes_pontok}")

print(f"Beolvasott sorok{':':>5} {hossz}")
print(f"Érvényes pontszám{':':>5} {erv_db}")
print(f"Ebből egyedi{':':>5} {erv_db-ismetlodes}")
print(f"Ismétlődés{':':>5} {ismetlodes}")
print(f"Hibás bejegyzés{':':>5} {len(hibas_pontok)}")
print(f"Rendezett lista{':':>5} {sorted(ervenyes_pontok, reverse = True)}")


