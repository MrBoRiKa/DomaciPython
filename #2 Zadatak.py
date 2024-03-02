#2 Zadatak

a = int(input("Unesite koeficijent a: "))
b = int(input("Unesite koeficijent b: "))
c = int(input("Unesite koeficijent c: "))

D = b**2 - 4*a*c

x1 = (int(-b) + int(D)**0.5) / (2*int(a))
x2 = (int(-b) - int(D)**0.5) / (2*int(a))


print(f'Vrijednosti x1 i x2 su :' ,x1 ,"i", x2)

#Prikazuje mi drugaciju vrijednost
