from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def weather():
    weather_data = {}
    if request.method == "POST":
        location = request.form.get("location")  # Get city name input from the user
        api_key = "297ecbcd89c1f3cfbef7f9a065b9d5f3"  # Replace with your actual OpenWeatherMap API key
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

        try:
            # Sending the API request to OpenWeatherMap
            response = requests.get(api_url)
            print("API URL:", api_url)  # Debugging: prints the API URL being called
            print("Response Status Code:", response.status_code)  # Debugging: prints the response status code

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": data["name"],  # City name from the response
                    "temperature": data["main"]["temp"],  # Temperature in Celsius
                    "humidity": data["main"]["humidity"],  # Humidity percentage
                    "description": data["weather"][0]["description"],  # Weather description
                }
            else:
                weather_data = {"error": f"Error {response.status_code}: {response.json().get('message', 'An error occurred.')}"}
        except Exception as e:
            weather_data = {"error": f"An error occurred: {e}"}

    return render_template("weather.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
