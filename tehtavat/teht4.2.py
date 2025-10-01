#1 tuuma = 2.54cm

tuuma = float(input("Anna tuumamäärä jonka haluat muuntaa (neg lopettaa): "))

while tuuma >= 0:
    #muunnetaan
    cm = tuuma * 2.54
    print(f"{tuuma} tuumaa on {cm} senttimetriä.")
    tuuma = float(input("Anna tuumamäärä jonka haluat muuntaa (neg lopettaa): "))

print("Ohjelma päättyi.")
