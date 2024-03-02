n_ucenici = int(input("Unesite broj ucenika koji su ucestvovali na prvoj strani: "))
k_ucenici = int(input("Unesite broj ucenika koji su ucestvovali na drugoj strani : "))
p1 = float(input('Prosjecni poeni za N ucenike'))
p2 = float(input('Prosjecni poeni za K ucenike'))

prosjecna_ocjena = ((n_ucenici * p1) + (k_ucenici*p2)) / (k_ucenici+n_ucenici)
print(f"{prosjecna_ocjena:.2f}")

