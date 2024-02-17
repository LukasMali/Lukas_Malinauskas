# Paprastas skaičiuotuvas su ciklu, įvedimo validacija ir funkcijų skaidymu

def sudetis(x, y):
    return x + y

def atimtis(x, y):
    return x - y

def daugyba(x, y):
    return x * y

def dalyba(x, y):
    if y == 0:
        return "Dalyba iš nulio negalima"
    else:
        return x / y

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
            rezultatas = sudetis(skaicius1, skaicius2)
        elif veiksmas == '-':
            rezultatas = atimtis(skaicius1, skaicius2)
        elif veiksmas == '*':
            rezultatas = daugyba(skaicius1, skaicius2)
        elif veiksmas == '/':
            rezultatas = dalyba(skaicius1, skaicius2)

        print(f"Rezultatas: {rezultatas}")

skaiciuoti()
