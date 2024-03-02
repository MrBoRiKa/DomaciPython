#Prvo postavljamo pocetne cijene

poc_cijena = int(input('Unesite cijenu Playstation-a 5: '))

prva_cijena = (poc_cijena * 0.1) + poc_cijena

druga_cijena =prva_cijena  -  (prva_cijena * 0.1) 

print(round(druga_cijena))