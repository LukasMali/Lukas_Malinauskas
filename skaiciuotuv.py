from flask import Flask, request, render_template_string

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    rezultatas = ""
    skaicius1 = None
    skaicius2 = None
    operacija = None
    if request.method == 'POST':
        operacija = request.form['operacija']
        skaicius1 = float(request.form.get('skaicius1', 0))
        if operacija in ['^2', 'sqrt']:
            if operacija == '^2':
                rezultatas = kvadratu(skaicius1)
            elif operacija == 'sqrt':
                rezultatas = saknis(skaicius1)
        else:
            skaicius2 = float(request.form.get('skaicius2', 0))
            if operacija == '+':
                rezultatas = sudetis(skaicius1, skaicius2)
            elif operacija == '-':
                rezultatas = atimtis(skaicius1, skaicius2)
            elif operacija == '*':
                rezultatas = daugyba(skaicius1, skaicius2)
            elif operacija == '/':
                rezultatas = dalyba(skaicius1, skaicius2)

    return render_template_string('''
    <html>
    <head>
        <script>
        function toggleInput(operacija) {
            var skaicius2Div = document.getElementById('skaicius2Div');
            if(operacija === '^2' || operacija === 'sqrt') {
                skaicius2Div.style.display = 'none';
            } else {
                skaicius2Div.style.display = 'block';
            }
        }
        </script>
    </head>
    <body onload="toggleInput(document.querySelector('select[name=operacija]').value)">
        <form method="post" onchange="toggleInput(this.operacija.value)">
            Skaicius 1: <input type="number" name="skaicius1" value="{{ skaicius1 }}"><br>
            <div id="skaicius2Div" style="display:block;">
                Skaicius 2: <input type="number" name="skaicius2" value="{{ skaicius2 }}"><br>
            </div>
            Operacija: <select name="operacija">
                <option value="+">Sudėtis</option>
                <option value="-">Atimtis</option>
                <option value="*">Daugyba</option>
                <option value="/">Dalyba</option>
                <option value="^2">Kėlimas kvadratu</option>
                <option value="sqrt">Šaknies traukimas</option>
            </select><br>
            <input type="submit" value="Skaičiuoti">
        </form>
        ''' + (f"<p>Jūsų įvestis: {skaicius1}" + (f", {skaicius2}" if skaicius2 is not None else "") + f". Operacija: {operacija}.<br>Rezultatas: {rezultatas}</p>" if operacija else "") + '''
    </body>
    </html>
    ''', skaicius1=skaicius1, skaicius2=skaicius2, operacija=operacija)

if __name__ == '__main__':
    app.run(debug=True)