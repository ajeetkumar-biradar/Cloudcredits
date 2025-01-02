from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# API configuration (replace with your API key)
API_URL = "https://api.exchangerate-api.com/v4/latest/"
BASE_CURRENCY = "USD"  # Default base currency

def get_exchange_rates(base_currency):
    """Fetch exchange rates for a base currency."""
    response = requests.get(f"{API_URL}{base_currency}")
    if response.status_code == 200:
        return response.json()
    return None

@app.route("/", methods=["GET", "POST"])
def currency_converter():
    result = None
    error = None
    rates = None

    if request.method == "POST":
        base_currency = request.form.get("base_currency")
        target_currency = request.form.get("target_currency")
        amount = request.form.get("amount")

        if not base_currency or not target_currency or not amount:
            error = "Please fill in all fields."
        else:
            try:
                amount = float(amount)
                exchange_data = get_exchange_rates(base_currency)
                if exchange_data and target_currency in exchange_data["rates"]:
                    rate = exchange_data["rates"][target_currency]
                    converted_amount = amount * rate
                    result = f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}"
                    rates = exchange_data["rates"]
                else:
                    error = "Unable to fetch exchange rate. Please check the currencies."
            except ValueError:
                error = "Invalid amount. Please enter a valid number."

    return render_template("index.html", result=result, error=error, rates=rates)

if __name__ == "__main__":
    app.run(debug=True)
