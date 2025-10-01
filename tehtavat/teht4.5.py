yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break
    else:
        print("Väärä tunnus tai salasana!")
        yritykset += 1

if yritykset == 5:
    print("Access denied.")

