broj = (int(input('Unesite cetvorocifreni broj:')))

prva_cifra = broj // 1000
druga_cifra = (broj % 1000) // 100
treca_cifra = (broj %100) // 10
cetvrta_cifra = broj % 10

kvd_zbir = (prva_cifra+druga_cifra+treca_cifra+cetvrta_cifra)**2

print('Rezultat je : ',kvd_zbir)