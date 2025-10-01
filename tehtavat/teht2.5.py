leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luoti_grammoina = 13.3
naula_grammoina = 32 * luoti_grammoina
leiviska_grammoina = 20 * naula_grammoina

massa_grammoina = (
    leiviskat * leiviska_grammoina +
    naulat * naula_grammoina +
    luodit * luoti_grammoina
)

#massa_grammoina = (leiviskat * 20 * 32 * 13.3) + (naulat * 32 * 13.3) + (luodit * 13.3)

kilot = int(massa_grammoina // 1000)
grammat = massa_grammoina % 1000

print(f"{kilot} kilogrammaa ja {grammat:.2f} grammaa.")


