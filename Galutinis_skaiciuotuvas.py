from flask import Flask, request, render_template_string
import matplotlib.pyplot as plt
import numpy as np
import io
import base64


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    equation = ""
    error = ""
    if request.method == 'POST':
        skaicius1_str = request.form.get('skaicius1', '0')  # Default to '0' if not found
        skaicius2_str = request.form.get('skaicius2', '0')  # Default to '0' for operations requiring a second input
        operacija = request.form.get('operacija')

        # Convert to float if the string is not empty, else default to 0
        skaicius1 = float(skaicius1_str) if skaicius1_str else 0
        skaicius2 = float(skaicius2_str) if skaicius2_str else 0
        
        # Construct the equation and compute the result
        if operacija == 'pow':
            result = skaicius1 ** skaicius2
            equation = f"{skaicius1} ^ {skaicius2}"
        elif operacija == 'sqrt':
            if skaicius1 < 0:
                error = "Negalima ištraukti šaknies iš neigiamo skaičiaus"
            else:
                result = skaicius1 ** 0.5
            equation = f"√{skaicius1}"
        elif operacija == '+':
            result = skaicius1 + skaicius2
            equation = f"{skaicius1} + {skaicius2}"
        elif operacija == '-':
            result = skaicius1 - skaicius2
            equation = f"{skaicius1} - {skaicius2}"
        elif operacija == '*':
            result = skaicius1 * skaicius2
            equation = f"{skaicius1} * {skaicius2}"
        elif operacija == '/':
            if skaicius2 == 0:
                error = "Dalyba iš nulio negalima"
            else:
                result = skaicius1 / skaicius2
            equation = f"{skaicius1} / {skaicius2}"

        # Only add the equals sign and result if there was no error
        if not isinstance(result, str):
            equation += f" = {result}"

    result_display = error if error else equation

    return render_template_string('''
    <html>
    <head>
        <title>Calculator</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f5f5f5;
            }
            .calculator {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                width: auto;
            }
            .calculator input[type="number"], .calculator select, .calculator button {
                width: 100%;
                padding: 10px;
                margin-bottom: 12px;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box; /* Ensures padding does not increase the width */
            }
            .calculator input[type="submit"], .calculator button[type="button"] {
                cursor: pointer;
                color: white;
                border: none;
                border-radius: 4px;
            }
            .calculator input[type="submit"] {
                background-color: #007bff;
            }
            .calculator input[type="submit"]:hover {
                background-color: #0056b3;
            }
            .calculator button[type="button"] {
                background-color: #dc3545;
                width: auto; /* Allows the button to shrink to fit its content */
            }
            .calculator button[type="button"]:hover {
                background-color: #c82333;
            }
            .result {
                font-size: 18px;
                margin-top: 12px;
            }
        </style>
        <script>
        function toggleInput(operacija) {
            var skaicius2Div = document.getElementById('skaicius2Div');
            var skaicius2Label = document.getElementById('skaicius2Label');
            if(operacija === 'sqrt') {
                skaicius2Div.style.display = 'none';
            } else {
                skaicius2Div.style.display = 'block';
                skaicius2Label.innerText = operacija === 'pow' ? 'Laipsnis:' : 'Skaičius 2:';
            }
        }
        </script>
    </head>
    <body onload="toggleInput(document.querySelector('select[name=operacija]').value)">
        <div class="calculator">
            <form method="post" onchange="toggleInput(this.operacija.value)">
                Skaičius 1: <input type="number" name="skaicius1" value=""><br>
                <div id="skaicius2Div" style="display:block;">
                    <label id="skaicius2Label" for="skaicius2">Skaičius 2:</label>
                    <input type="number" name="skaicius2" id="skaicius2" value=""><br>
                </div>
                Operacija: <select name="operacija">
                    <option value="+">Sudėtis</option>
                    <option value="-">Atimtis</option>
                    <option value="*">Daugyba</option>
                    <option value="/">Dalyba</option>
                    <option value="pow">Kėlimas laipsniu</option>
                    <option value="sqrt">Šaknies traukimas</option>
                </select><br>
                <input type="submit" value="Skaičiuoti">
            </form>
            {{result_html|safe}}
            <div class="result">{{result_display}}</div>
            <a href="/plot">Braižyti funkcijos grafiką</a>
        </div>
    </body>
    </html>
    ''', result_display=result_display)

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    function_input = ""  # Initialize variable to hold the function input
    graph_html = ""      # Initialize variable to hold graph HTML
    error_message = ""   # Initialize variable to hold potential error messages
    if request.method == 'POST':
        try:
            function_input = request.form['function']
            
            # Preprocessing input for evaluation
            function_input = function_input.replace("^", "**").replace("sin", "np.sin").replace("cos", "np.cos").replace("tan", "np.tan").replace("sqrt", "np.sqrt").replace("log", "np.log")

            # Prepare the x values
            x = np.linspace(-10, 10, 400)
            
            # Evaluate the function safely
            y = eval(function_input, {"x": x, "np": np, "__builtins__": None}, {})
            
            # Plotting
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set(xlabel='x', ylabel='f(x)', title='Funkcijos grafikas')
            ax.axhline(0, color='black', lw=1)  # Draw x-axis
            ax.axvline(0, color='black', lw=1)  # Draw y-axis
            ax.grid()

            # Convert plot to PNG image
            img = io.BytesIO()
            plt.savefig(img, format='png', bbox_inches='tight')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')

            graph_html = f'<img src="data:image/png;base64,{plot_url}">'
        except Exception as e:
            graph_html = f"<p>Įvyko klaida: {e}</p>"
    else:
        graph_html = "<p>Įveskite funkciją ir paspauskite 'Brėžti'.</p>"
    
    # The form and buttons are shown regardless of whether there's a POST request
    html_content = f'''
    <html>
    <head>
        <title>Function Plotter</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 20px;
            }}
            .plotter {{
                margin: auto;
                width: 50%;
                padding: 10px;
            }}
            .button {{
                margin: 5px;
                padding: 10px 15px;
                border-radius: 5px;
                border: 1px solid #ddd;
                background-color: #f8f8f8;
                cursor: pointer;
                display: inline-block;
            }}
            .button.function {{
                background-color: #e7f4e4;
            }}
            .button.clear {{
                background-color: #fee;
            }}
            .button.plot {{
                background-color: #eef;
            }}
            .error {{
                color: red;
            }}
        </style>
        <script>
            function insertSymbol(symbol) {{
                var input = document.getElementById('function');
                var cursorPos = input.selectionStart;
                var v = input.value;
                var textBefore = v.substring(0, cursorPos);
                var textAfter  = v.substring(cursorPos, v.length);

                input.value = textBefore + symbol + textAfter;
                input.selectionStart = cursorPos + symbol.length;
                input.selectionEnd = cursorPos + symbol.length;
                input.focus();
            }}
            function clearInput() {{
                document.getElementById('function').value = '';
            }}
        </script>
    </head>
    <body>
        <div class="plotter">
            <h2>Grafinis funkcijų sprendimas</h2>
            <form method="POST">
                Funkcija f(x)= <input type="text" id="function" name="function" value="{function_input}" placeholder="e.g., x^2 + 2*x + 1"><br>
                <div class="buttons">
                    <span class="button function" onclick="insertSymbol('sqrt(')">√()</span>
                    <span class="button function" onclick="insertSymbol('log(')">log()</span>
                    <span class="button function" onclick="insertSymbol('^')">^</span>
                    <span class="button function" onclick="insertSymbol('*')">x</span>
                     <span class="button function" onclick="insertSymbol('/')">÷</span>
                    <span class="button function" onclick="insertSymbol('sin(')">sin()</span>
                    <span class="button function" onclick="insertSymbol('cos(')">cos()</span>
                    <span class="button function" onclick="insertSymbol('tan(')">tan()</span>
                    <!-- Additional function buttons as needed -->
                </div>
                <input class="button plot" type="submit" value="Brėžti">
                <span class="button clear" onclick="clearInput()">Išvalyti</span>
            </form>
            {graph_html}  <!-- This will display the graph image -->
            <div>
                {error_message}  <!-- This will display any error message -->
            </div>
        </div>
        <a href="/">Grįžti prie skaičiuotuvo</a>
    </body>
</html>
'''

    return html_content


if __name__ == '__main__':
    app.run(debug=True)