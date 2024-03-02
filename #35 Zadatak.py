broj_jedinice = int(input('Unesite stambenu jedincu: '))
srednja_cifra = (broj_jedinice % 1000)// 100
peta_cifra = broj_jedinice % 10

jedinica = srednja_cifra+ peta_cifra
print('Jedinica se nalazi na ', jedinica,'spratu')