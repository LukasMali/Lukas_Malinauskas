# Paprastas skaičiuotuvas su ciklu

def skaiciuoti():
    while True:  # Pridedamas ciklas, leidžiantis kartoti skaičiavimus
        veiksmas = input("Pasirinkite veiksmą (+, -, *, /) arba 'q' jei norite baigti: ")
        if veiksmas == 'q':  # Leidžia vartotojui išeiti iš programos
            print("Programa baigta.")
            break

        if veiksmas not in ['+', '-', '*', '/']:
            print("Nepalaikomas veiksmas. Bandykite dar kartą.")
            continue

        skaicius1 = float(input("Įveskite pirmą skaičių: "))
        skaicius2 = float(input("Įveskite antrą skaičių: "))

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
