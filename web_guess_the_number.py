from flask import Flask, request, render_template_string
import random

app = Flask(__name__)
target_number = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def index():
    global target_number
    feedback = ""
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            if guess < target_number:
                feedback = "Too low! Try again."
            elif guess > target_number:
                feedback = "Too high! Try again."
            else:
                feedback = "Correct! You guessed the number."
                target_number = random.randint(1, 100)  # Reset the game
        except ValueError:
            feedback = "Please enter a valid number."
    
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Guess the Number Game</title>
          </head>
          <body>
            <div style="text-align: center; margin-top: 50px;">
              <h1>Guess the Number Game</h1>
              <form method="post">
                <input type="text" name="guess" placeholder="Enter your guess">
                <button type="submit">Submit Guess</button>
              </form>
              <p>{{ feedback }}</p>
            </div>
          </body>
        </html>
    ''', feedback=feedback)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
