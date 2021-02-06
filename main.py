from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    centimeter = request.args.get("centimeter", "")
    if centimeter:
        inches = inches_from(centimeter)
    else:
        inches = ""
    return (
        """<form action="" method="get">
                Centimetrs: <input type="text" name="centimeter">
                <input type="submit" value="Convert to Inches">
            </form>"""
        + "Inches: "
        + inches
    )

def inches_from(centimeter):
    """Convert Centimeter to Inches."""
    try:
        inches = float(centimeter) / 2.54
        inches = round(inches, 3)  # Round to three decimal places
        return str(inches)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)