from math import *
#Ülesanne 1
#Kirjuta programm, mis sind tervitab ja kuvab ekraanile tänane kuupäev 
#moduli datetime kasutades ja date.today() funktsiooni abil.
from datetime import *
tana=date.today()
print(f"Tere! Täna on {tana}")

#Kasuta erinevate formaatide kuvamiseks ekraanile järgmised funktsioonid:

# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(tana1)
# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(tana2)
# 12/27/22
tana3 = tana.strftime("%m/%d/%y")
print(tana3)
# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(tana4)
# Omadused day, month, year kasutatakse päeva, 
# kuu ja aasta parameetri leidmiseks date klassist.
# Arvuta mitu päeva on jäänud kuu lõpuni, aasta lõpuni.
# Arvuta oma vanus aastates, kuudes ja päevades.
aasta=tana.year
kuu=tana.month
paev=tana.day
print(f"Tänane aasta: {aasta}, kuu: {kuu}, päev: {paev}")
kuulõpuni=date(aasta, kuu+1, 1) - tana
aastalõpuni=date(aasta+1, 1, 1) - tana
print(f"Jäänud päevi kuu lõpuni: {kuulõpuni.days}")
print(f"Jäänud päevi aasta lõpuni: {aastalõpuni.days}")

# Arvuta oma vanus aastates, kuudes ja päevades. Tee ise.
#Ülesanne 2
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt 
# ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.
print("Tehe 3 + 8 / (4 - 2) * 4", 3 + 8 / (4 - 2) * 4)

#Ülesanne 3
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile 
# ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.
try:
    R=float(input("Sisesta ringi raadius R: "))
    ruudu_pindala=(2*R)**2
    ruudu_ymbermoot=4*(2*R)
    ringi_pindala=pi*R**2
    ringi_ymbermoot=2*pi*R
    print(f"Ruudu pindala: {ruudu_pindala}, \nruudu ümbermõõt: {ruudu_ymbermoot}, \nringi pindala: {ringi_pindala}, \nringi ümbermõõt: {ringi_ymbermoot}")
except ValueError:
    print("Palun sisesta kehtiv arv.")

#Ülesanne 4
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides 
# ehk teisisõnu: kui palju 2-euroseid münte tuleb panna üksteise kõrvale, 
# et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.

# Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses 
# sisukate nimedega muutujatele. 
# Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), 
# siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.  
# Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda
# (teisendamised, ümardamise täpsus jne). Võimalusel võrrelge tulemusi teistega.
# Kui on erinevusi, leidke ühiselt põhjused.
# Kas programm on piisavalt hästi kirjutatud, 
# et algandmete muutumise korral (näiteks juhul, 
# kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?
Maa_raadius=6378  # km
Mundi_dia=2  # cm

Maa_ymbermoot=2*pi*Maa_raadius*1000  # cm
Mundi_arv=Maa_ymbermoot/Mundi_dia
print(f"2-euroseid münte on vaja: {Mundi_arv:.0f}") #Kas lahendus on õige?
