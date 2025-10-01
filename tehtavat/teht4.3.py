luku = input("Anna luku, tyhjä lopettaa: ")

pieni = luku
suuri = luku

while luku != "":
    numero = int(luku)

    #Vertaillaan pientä ja suurta
    if pieni == luku or numero < pieni:
        pieni = numero

    if suuri == luku or numero > suuri:
        suuri = numero

    luku = input("Anna luku, tyhjä lopettaa: ")

print(f"Pienin luku on {pieni}")
print(f"Suurin luku on {suuri}")