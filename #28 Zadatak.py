cifra = int(input('Unesite trocifreni broj:'))

prva_c = cifra//100
druga_c= (cifra%100) //10
treca_c = cifra % 10

print(str(treca_c)+str(druga_c)+str(prva_c))