print("-----Tervetuloa käyttämään laskinta!-----")
print("Valitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku"
      "\n C: Kertolasku \n D: Jakolasku")

valinta = input("Valintasi (A - D): ").upper()

if valinta == "A":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Yhteenlasku:", a + b)
elif valinta == "B":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Vähennyslasku:", a - b)
elif valinta == "C":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Kertolasku:", a * b)
elif valinta == "D":
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    print("Desimaalijakolasku:", a / b)
else:
    print("Valintasi oli virheellinen.")

