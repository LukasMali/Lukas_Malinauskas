# Paprastas skaičiuotuvas su vartotojo sąsajos meniu

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

def rodyti_meniu():
    print("""
    Pasirinkite veiksmą iš meniu:
    +   - Sudėtis
    -   - Atimtis
    *   - Daugyba
    /   - Dalyba
    ^2  - Kėlimas kvadratu
    sqrt - Šaknies traukimas
    q   - Baigti programą
    """)

def skaiciuoti():
    while True:
        rodyti_meniu()
        veiksmas = input("Jūsų pasirinkimas: ")
        if veiksmas == 'q':
            print("Programa baigta. Ačiū, kad naudojotės!")
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
            rezultatas = kvadratu(skaicius) if veiksmas == '^2' else saknis(skaicius)
        else:
            try:
                skaicius1 = float(input("Įveskite pirmą skaičių: "))
                skaicius2 = float(input("Įveskite antrą skaičių: "))
            except ValueError:
                print("Netinkamas įvedimas. Būtina įvesti skaičių. Bandykite iš naujo.")
                continue

            rezultatas = {
                '+': sudetis,
                '-': atimtis,
                '*': daugyba,
                '/': dalyba
            }.get(veiksmas)(skaicius1, skaicius2)

        print(f"Rezultatas: {rezultatas}")

skaiciuoti()
