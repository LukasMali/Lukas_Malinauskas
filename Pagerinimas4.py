# Paprastas skaičiuotuvas su papildomomis matematinėmis operacijomis

def sudetis(x, y):
    return x + y

def atimtis(x, y):
    return x - y

def daugyba(x, y):
    return x * y

def dalyba(x, y):
    if y == 0:
        return "Dalyba iš nulio negalima"
    return x / y

def kvadratu(x):
    return x ** 2

def saknis(x):
    if x < 0:
        return "Negalima ištraukti šaknies iš neigiamo skaičiaus"
    return x ** 0.5

def skaiciuoti():
    while True:
        veiksmas = input("Pasirinkite veiksmą (+, -, *, /, ^2, sqrt) arba 'q' jei norite baigti: ")
        if veiksmas == 'q':
            print("Programa baigta.")
            break

        if veiksmas not in ['+', '-', '*', '/', '^2', 'sqrt']:
            print("Nepalaikomas veiksmas. Bandykite dar kartą.")
            continue

        if veiksmas in ['^2', 'sqrt']:
            try:
                skaicius = float(input("Įveskite skaičių: "))
            except ValueError:
                print("Netinkamas įvedimas. Būtina įvesti skaičių. Bandykite iš naujo.")
                continue
            if veiksmas == '^2':
                rezultatas = kvadratu(skaicius)
            elif veiksmas == 'sqrt':
                rezultatas = saknis(skaicius)
        else:
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
