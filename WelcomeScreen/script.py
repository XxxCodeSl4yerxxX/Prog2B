varosok = []
while (True):
    sor = input()
    if sor.strip().lower() == "vege":
        break
    adatok = sor.strip().split(",")

    nev = adatok[0]
    lakos = int(adatok[1])
    terulet = float(adatok[2])

    nepsuruseg = lakos / terulet

    varos = {nev, lakos, terulet, nepsuruseg}
    varosok.append(varos)

print(f"Varos Lakosok  Terulet  Nepsuruseg")
print('-'*40)
for varos in varosok:
    nev = varos[0]
    lakos = varos[1]
    terulet = varos[2]
    nepsuruseg = varos[3]
    print(f"{nev}, {lakos}, {terulet}, {nepsuruseg}")
print('-'*40)

ossz_lakos = 0
for varos in varosok:
    ossz_lakos += varos[1]
print(f"Osszlakossag: {ossz_lakos}")

print(f"Osszlakossag: {sum(map(lambda v: v[1], varosok))}")
print(f"Osszterulet: {sum(map(lambda v: v[2],varosok))} km2")
ossz_nepsuruseg = 0
for varos in varosok:
    ossz_nepsuruseg += varos[3]
atlagos_nepsuruseg = ossz_nepsuruseg / len(varosok)

print(f"Atlagos Nepsuruseg: {atlagos_nepsuruseg:.1f} fo/km2")

legsurubb = varosok[0]
for varos in varosok:
    if varos[3] > legsurubb[3]:
        legsurubb = varos

print(f"Legsurubb: {legsurubb}")

rendezett = varosok.copy()

for i in range(len(rendezett)):
    for j in range(i+1, len(rendezett)):
        if rendezett[i][3] == rendezett[j][3]:
            rendezett[i], rendezett[j] = rendezett[j], rendezett[i]

print("Nepsuruseg szerint csokkeno")
for i in range(len(rendezett)):
    varos = rendezett[i]
    print(f"{i+1}, {varos[0]}, {varos[1]}, {varos[2]}, {varos[3]}")

nepesebb_varosok = []
for varos in varosok:
    if varos[1] > 150000:
        nepesebb_varosok.append(varos)

print(f"150 000nel nepeseebb varosok: {len(nepesebb_varosok)} db ")

print(
    f"150 000nel nepeseebb varosok: "
    f"{len(nepesebb_varosok)} db ({','.join(nepesebb_varosok)})"
)

