# print("Hello, \nWorld!") # 2 rida
# print("Tere tulemast\t!")
# print("Õpin",1,".kursusel") #sep=" " vaikimisi on tühik


# #Paremetrid sep ja end
# print() #see on tühi rida
# print("Õpin",1,".kursusel",sep="***") #sep="" tähendab, et tühikut ei ole
# print("2026", "10", "01", sep="/")
# print("Sama ", end="") #end="" tähendab, et reavahetust ei ole end="\n"
# print("rida")


# #Muutujad
# nimi = "Python" #str ehk sõne
# print("Tere,", nimi)
# kursus=1
# print("Õpin",kursus,".kursusel")

# # input() funktsioon
# nimi = input("Sisesta oma nimi: ") #programm küsib ja ootab kasutaja sisestust
# print("Tere,", nimi)
# kursus=int(input("Sisesta kursuse number: ")) #teisendab sõne arvuks
# print("Õpin",kursus,".kursusel")
# print("Järgmisel aastan õpin ",kursus+1,".kursusel") 
# #kursus+1 tähendab, et kursuse number suureneb 1 võrra")

# print("Liitmine")
# a =float(input("Esimene arv: "))
# b =float(input("Teine arv: "))
# print(a,"+",b,"=",a + b)

# print("Lahutamine")
# a =float(input("Esimene arv: "))
# b =float(input("Teine arv: "))
# print(a,"-",b,"=",a - b)
# # tee ka ise korrutamine ja jagamine

# print("Jagamine")
# a =float(input("Esimene arv: "))
# b =float(input("Teine arv: "))
# print(a,"/",b,"=",a / b)
# print("Ümardatud arv:",round(a / b,2))

#f-sõne formatimine
nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")

a =float(input("Esimene arv: "))
tehe=input("Tehe: ")
b =float(input("Teine arv: "))

print(f"{a} {tehe} {b} = {eval(f'{a} {tehe} {b}')}")