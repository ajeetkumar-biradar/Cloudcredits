from flask import Flask, request, render_template
import random

app = Flask(__name__)

target_number = random.randint(1, 100)
attempts = 10

@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    global target_number, attempts
    message = ""

    if request.method == "POST":
        guess = request.form.get("guess")

        if guess is None or guess.strip() == "":
            message = "Please enter a number to make a guess."
        else:
            try:
                guess = int(guess)

                if guess < 1 or guess > 100:
                    message = "Please guess a number between 1 and 100."
                elif guess < target_number:
                    message = "Too low! Try again."
                    attempts -= 1
                elif guess > target_number:
                    message = "Too high! Try again."
                    attempts -= 1
                else:
                    message = f"Congratulations! You've guessed the number {target_number} correctly."
                    target_number = random.randint(1, 100)
                    attempts = 10

                if attempts == 0:
                    message = f"Sorry, you've run out of attempts. The correct number was {target_number}. A new number has been generated."
                    target_number = random.randint(1, 100)
                    attempts = 10

            except ValueError:
                message = "Invalid input. Please enter a valid number."

    return render_template("index.html", message=message, attempts=attempts)

if __name__ == "__main__":
    app.run(debug=True)
