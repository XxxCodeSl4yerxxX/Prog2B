matrix = []
n = 0

def kiir (matrix,m, szoveg):
    print(szoveg)
    for sor in matrix:
        for elem in sor:
            print(elem, end=" ")
        print()
    print()

with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    print(n)
    for sor in f:
        #print(sor)
        listastr = sor.strip().split(" ")
        #print(listastr)
        listaint = []
        for elem in listastr:
            listaint.append(int(elem))
        matrix.append(listaint)
print(matrix)

'''
matrix2 = []
n2 = int(input("Add meg a matrix meretet: "))

for i in range(n2):
    sor = list(map(int(input()).strip().split(" ")))
    matrix2.append(sor)
print(n)
print(matrix2)
'''

transzponalt = []
for i in range(n):
    sor = []
    for j in range(n):
        sor.append(matrix[j][i])
    transzponalt.append(sor)

kiir(matrix,n,"4es feladat matrixja")
kiir(transzponalt,n,"4es feladat transzponaltja")

sorok = len(matrix)
oszlop = len(matrix[0])

if sorok == oszlop:
    print("Negyzetes :D")
else:
    print("Nem negyzetes :(")

ElteresDB = 0
elem_i = -1
elem_j = -1

for i in range(n):
    for j in range(i+1,n):
        if matrix[i][j] != matrix[j][i]:
            ElteresDB += 1

            if elem_i == -1:
                elem_i = i
                elem_j = j

if ElteresDB == 0:
    print("Szimetrikus a matrix a transzponaltal")
else:
    print("Nem szometrikus")
    print(f"Eltero szamok: {ElteresDB} db")
    print(f"Az elso elteres, sor: {elem_i+1} oszlop: {elem_j+1} ({matrix[elem_i][elem_j]},{matrix[elem_j][elem_i]}) <-> {elem_j+1} {elem_i+1}")