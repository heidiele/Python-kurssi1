pituus = float(input("Anna pituutesi: "))
paino = float(input("Anna painosi: "))

#Muuttuja jossa lasku suoritetaan
bmi = paino / (pituus / 100) ** 2

print("Pituus-paino-indeksisi on", bmi)
print(f"Pituus-paino-indeksisi on {bmi:.2f}")


