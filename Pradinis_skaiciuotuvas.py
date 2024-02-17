# Paprastas skaičiuotuvas

def skaiciuoti():
    veiksmas = input("Pasirinkite veiksmą (+, -, *, /): ")
    if veiksmas not in ['+', '-', '*', '/']:
        print("Nepalaikomas veiksmas")
        return

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
