from flask import Flask
from flask import request, escape

app = Flask(__name__)


@app.route("/")
def index():
    celsius = request.args.get("celsius", "") # get value of key = "celsius", else empty str
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""

    return ( 
        """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
              </form>"""
              + "fahrenheit: "
              + fahrenheit

    )

# Use <> to indicate the value inside is passed to the function below
# with the same variable name
# `int:` to instruct Flask to check if the value can be converted to integer
# if not, Not Found error is displayed

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
