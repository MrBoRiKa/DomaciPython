broj = (int(input('Unesite cetvorocifreni broj:')))

prva_cifra = broj // 1000
druga_cifra = (broj % 1000) // 100
treca_cifra = (broj %100) // 10
cetvrta_cifra = broj % 10

kvr_zbira = prva_cifra**2 + 2*prva_cifra*cetvrta_cifra + cetvrta_cifra**2
raz_kvr = (druga_cifra-treca_cifra)*(druga_cifra+treca_cifra)

krajnji_zbir =kvr_zbira - raz_kvr

print(round(krajnji_zbir))