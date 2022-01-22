'''
4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! 
Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
'''

lista = []

def kerulet(a, b):
    elemzo = 0
    if b != '':
        for i in b:
            elemzo +=1
    elif b == '':
        a = 4*a
        return print(f"A négyzet kerülete: {a} cm")
    elif elemzo == 1:
        ertek = 0
        osszeg = 0
        for i in b:
            ertek = i
        osszeg = a + ertek
        osszeg = osszeg*2
        return print(f"A téglalap kerülete: {osszeg} cm")
    elif elemzo == 2:
        osszeg = 0
        b.append(a)
        for i in b:
            osszeg += i
        return print(f"A hármszög kerülete: {osszeg} cm")
    elif elemzo > 2:
        osszeg = 0
        b.append(a)
        for i in b:
            osszeg += i
        return print(f"A sokszög kerülete: {osszeg} cm")




print("négyzet")
print("téglalap")
print("hármszög")
print("sokszög")
print("")
while True:
    bekeres = input("Milyen síkidomról van szó? ")
    if bekeres == "négyzet":
        bekeres = int(input("Mennyi a négyzet oldala? "))
        kerulet(bekeres, '')
        break
    elif bekeres == "téglalap":
        ertek1 = int(input("A téglalap egyik értéke "))
        ertek2 = int(input("A téglalap egyik értéke "))
        lista.append(ertek2)
        kerulet(ertek1, lista)
        break
    elif bekeres == "hármszög":
        ertek1 = int(input("A hármszög egyik értéke "))
        ertek2 = int(input("A hármszög egyik értéke "))
        ertek3 = int(input("A hármszög egyik értéke "))
        lista.append(ertek2)
        lista.append(ertek3)
        kerulet(ertek1, lista)
        break
    elif bekeres == "sokszög":
        ertek1 = int(input("A sokszög egyik értéke "))
        while True:
            ertek2 = int(input("A sokszög egyik értéke "))
            if ertek2 < 0:
                kerulet(ertek1, lista)
                break
            else:
                lista.append(ertek2)
        break


