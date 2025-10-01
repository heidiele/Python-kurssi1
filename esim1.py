age = int(input("Anna ikäsi: "))

if age >= 65:
    print("Olet eläkeiässä.")
elif age >= 18:
    print("Olet työikäinen.")
elif age >= 7:
    print("olet kouluikäinen.")
else:
    print("Olet pikkulapsi.")

print("Suoritus jatkuu...")