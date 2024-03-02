broj = (int(input('Unesite trocifreni broj:')))

prva_cifra = broj // 100
druga_cifra = (broj % 100) // 10
treca_cifra = broj %10
summ = prva_cifra + druga_cifra + treca_cifra

print(round(summ))