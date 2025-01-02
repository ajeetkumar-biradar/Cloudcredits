from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    """Calculate BMI using the formula: BMI = weight / (height^2)."""
    return weight / (height ** 2)

def interpret_bmi(bmi):
    """Interpret BMI value into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    error = None

    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])

            # Convert height to meters if input is in feet
            if request.form.get('height_unit') == 'feet':
                height = height * 0.3048

            # Convert weight to kilograms if input is in pounds
            if request.form.get('weight_unit') == 'lbs':
                weight = weight * 0.453592

            bmi = calculate_bmi(weight, height)
            category = interpret_bmi(bmi)
        except ValueError:
            error = "Please provide valid numerical inputs for weight and height."

    return render_template('index.html', bmi=bmi, category=category, error=error)

if __name__ == '__main__':
    app.run(debug=True)
