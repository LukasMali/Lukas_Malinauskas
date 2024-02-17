# Paprastas skaičiuotuvas su ciklu ir įvedimo validacija

def skaiciuoti():
    while True:
        veiksmas = input("Pasirinkite veiksmą (+, -, *, /) arba 'q' jei norite baigti: ")
        if veiksmas == 'q':
            print("Programa baigta.")
            break

        if veiksmas not in ['+', '-', '*', '/']:
            print("Nepalaikomas veiksmas. Bandykite dar kartą.")
            continue

        try:
            skaicius1 = float(input("Įveskite pirmą skaičių: "))
            skaicius2 = float(input("Įveskite antrą skaičių: "))
        except ValueError:
            print("Netinkamas įvedimas. Būtina įvesti skaičių. Bandykite iš naujo.")
            continue

        if veiksmas == '+':
            print(f"{skaicius1} + {skaicius2} = {skaicius1 + skaicius2}")
        elif veiksmas == '-':
            print(f"{skaicius1} - {skaicius2} = {skaicius1 - skaicius2}")
        elif veiksmas == '*':
            print(f"{skaicius1} * {skaicius2} = {skaicius1 * skaicius2}")
        elif veiksmas == '/':
            if skaicius2 != 0:
                print(f"{skaicius1} / {skaicius2} = {skaicius1 / skaicius2}")
            else:
                print("Dalyba iš nulio negalima")

skaiciuoti()
