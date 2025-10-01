import random

#Kysytään käyttäjältä kuinka monta pistettä arvotaan
N = int(input("Kuinka monta pistettä arvotaan: "))

n = 0          #monta pistettä onympyrän sisällä
laskuri = 0    #laskee kuinka monta pistettä on arvottu

#Arvotaan pisteitä niin kauan kunnes määrä N täyttyy
while laskuri < N:
    #Arvotaan satunnaiset koordinaatit x ja y neliöstä (-1..1, -1..1)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    #Testataan, jääkö piste yksikköympyrän sisälle
    #Ehto: x^2 + y^2 < 1
    if x*x + y*y < 1:
        n = n + 1  #lisätään n yhdellä, jos piste on ympyrässä

    laskuri = laskuri + 1  #kasvatetaan arvottujen pisteiden kokonaismäärää

#Lasketaan piin likiarvo kaavalla 4 * (ympyrän pisteitä) / (kaikki pisteet)
pii = 4 * n / N

#Tulostetaan tulos käyttäjälle
print("Piin likiarvo on:", pii)
