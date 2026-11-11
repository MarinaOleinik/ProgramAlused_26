# 1 Juku kinno
# Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, 
# muidu teatatakse, et täna kinno ei minda.
# Programm peab Juku ära tundma ka siis, 
# kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, 
# lisa märkus „Ära karju, Juku!“.
eesnimi=input("Sisesta eesnimi: ")
if eesnimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    if eesnimi == "JUKU":
        print("Ära karju, Juku!")
    #Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta:
    vanus=input("Sisesta Juku vanus: ")
    if vanus.isdigit():
        vanus=int(vanus)
        if vanus < 6:
            pilet="tasutapilet"
        elif 6 <= vanus <= 14:
            pilet="lastepilet"
        elif 15 < vanus < 65:
            pilet="täispilet"
        elif vanus >= 65:
            pilet="sooduspilet"
        else:
            print("Viga andmetes.")
        print(f"Juku vanus on {vanus} aastat, seega on vaja osta {pilet}.")
    else:
        print("Palun sisesta vanus numbrina.")
else:
    print("Täna kinno ei minda.")

# 2 Pinginaabrid
# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. 
# Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. 
# Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# Otsusta ise, kuidas „pinginaabrid“ määratakse, 
# näiteks juhuslikult või nimede algustähtede järgi.
# Kasuta: isalpha(), capitalize()
nimi1=input("Sisesta esimese inimese nimi: ")
nimi2=input("Sisesta teise inimese nimi: ")
print(f"Tere {nimi1.capitalize()} ja {nimi2.capitalize()}")
if nimi1.isalpha() and nimi2.isalpha():
    if nimi1 in ["Joonas", "Kenneth"] and nimi2 in ["Joonas", "Kenneth"]:
        print(f"Inimesed {nimi1.capitalize()} ja {nimi2.capitalize()} on täna pinginaabrid.")
    else:
        print("Inimesed ei ole täna pinginaabrid.")
else:
    print("Palun sisesta nimed õigesti.")

# 3. Remont
# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. 
# Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? 
# Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
# Kasuta: float(), lower() (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()

pikkus=float(input("Sisesta toa pikkus meetrites: "))
laius=float(input("Sisesta toa laius meetrites: "))
pindala=pikkus*laius
print(f"Toa pindala on {pindala} ruutmeetrit.")
remont=input("Kas soovid remonti teha? (Jah/Ei) ")
if remont.lower() == "jah":
    rm_hind=float(input("Sisesta ruutmeetri hind: "))
    remont_hind=pindala*rm_hind
    print(f"Põranda vahetamise hind on {remont_hind} eurot.")
    prof=input("Kas kasutad professionaali abi? (Jah/Ei) ")
    if prof.lower() == "jah":
        too_hind=float(input("Sisesta töö hind ruutmeetri kohta: "))
        koguhind=remont_hind + (pindala*too_hind)
        print(f"Remondi koguhind koos tööga on {round(koguhind,2)} eurot.")
else:
    print("Remonti ei tehta.")