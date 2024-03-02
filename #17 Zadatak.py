stara_cijena = int(input('Unesite staru cijenu knjige : '))
popust_knjige = int(input('Unesite popust na knjizi: '))
popust = popust_knjige/100

nova_cijena = stara_cijena * popust

print(round(nova_cijena))