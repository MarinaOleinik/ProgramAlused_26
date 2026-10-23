from random import *  #randint
from math import *  #pi
# # Kirjuta enda esimene programm, mis väljastab käsureale teksti: 
# #     “Tere, maailm!”. 
# # Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: 
# #     “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# # Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# # “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
# #Ülesanne1
print("Tere, maailm!")
nimi=input("Sisesta oma nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try:
    vanus=int(input("Sisesta oma vanus: "))
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun sisesta kehtiv number vanuse jaoks.")

#     # Ülesanne 2 
# # on järgnevad muutujad:
# # a) vanus = 18
# # b) eesnimi = "Jaak"
# # c) pikkus = 16.5
# # d) kas_käib_koolis = True
# # Mis võimalus veel peale True oleks viimast muutujat väärtustada? 
# # Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# # Kirjuta kood tüüpide kontrollimiseks.
# vanus=18 #int-täisarv
# eesnimi="Jaak" #str-sõne
# pikkus=16.5 #float-kümnendmurd/ujukomaarv
# kas_käib_koolis=True #bool-tõeväärtus
# print(f"Vanus:{vanus}, tüüp:{type(vanus)}")
# print(f"Eesnimi:{eesnimi}, tüüp:{type(eesnimi)}")
# print(f"Pikkus:{pikkus}, tüüp:{type(pikkus)}")
# print(f"Käib koolis:{kas_käib_koolis}, tüüp:{type(kas_käib_koolis)}")

# #Ülesanne 3
# # Kirjuta enda koodis laual olevate kommide arv muutujasse
# # (kommide arv on juhuslik). 
# # Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# # Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
# # Eemalda soovitud kommide arv laual olevate kommide arvust 
# # ja kuva ekraanile, 
# # kui palju komme laual nüüd on.

kommide_arv=randint(1, 100)  #int(input("Kommide arv: "))
print(f"Laud on {kommide_arv} kommi.")
try:
    kommid=int(input("Mitu kommi soovid ära võtta? "))
    kommide_arv -= kommid
    print(f"Laud on nüüd {kommide_arv} kommi.")
except ValueError:
    print("Palun sisesta number.")

# #Ülesanne 4
# #Puu läbimõõdu arvutamine
# # Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu 
# # ning teatab selle peale puu läbimõõdu.
ümbermõõt=float(input("Sisesta puu ümbermõõt: "))
läbimõõt=round(ümbermõõt/pi,1)
print(f"Puu läbimõõt on {läbimõõt}.")

#Ülesanne 5
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise 
#maatüki diagonaal, 
#mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
try:
    N=float(input("Sisesta ristküliku esimene külg (N): "))
    M=float(input("Sisesta ristküliku teine külg (M): "))

    diagonaal=round(sqrt(N**2 + M**2), 1) # sqrt() math moodulist
    print(f"Ristküliku diagonaal on {diagonaal}.")
except ValueError:
    print("Palun sisesta kehtiv number.")
#Ülesanne 7
#Koostada programm, mis arvutab aritmeetilise keskmise
# suvalisest etteantud 5 täis arvust.
#Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, 
#täisarvuline osa ja jääk.
arv1=randint(1, 100)
arv2=randint(1, 100)
arv3=randint(1, 100)
arv4=randint(1, 100)
arv5=randint(1, 100)
summa=arv1+arv2+arv3+arv4+arv5
keskmine=summa/5
print(f"Summa: {summa}, Keskmine: {keskmine}")
try:
    jagaja=int(input("Sisesta arv, millega jagada: "))
    tulemus=summa/jagaja
    print("Tulemus:", tulemus) #tulemus=3.75
    print("Täisarvuline osa:", int(tulemus)) 
    #int(3.75)=3 teine variant täisosa leidmiseks on kasutada // jagamist: summa//jagaja
    print("Jääk:", summa % jagaja)
except ValueError:
     print("Palun sisesta kehtiv number.")