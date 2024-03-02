d = int(input("Unesite dužinu terena u metrima: "))
s = int(input("Unesite širinu terena u metrima: "))
r = int(input("Unesite rastojanje ograde od terena u metrima: "))

duzina_ograde = 2 * (d + s) + 4 * r

print('Duzina ograde je:', duzina_ograde,' metara.')