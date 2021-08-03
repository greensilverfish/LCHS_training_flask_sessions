from flask import Flask, request, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'dj~fal*kduu9^032>8e?3ookso('

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        still_guessing = True
        guess = request.form["guess"]
        if guess < magic_number:
            low_value = guess
            message = f'{guess} is too low!'
        elif guess > magic_number:
            high_value = guess
            message = f'{guess} is too high!'
        elif guess == magic_number:
            message = f'Congratulations {guess} is the correct number! You Won!'
        else:
            message = f'Please enter a valid number!'
            still_guessing = False

    else:
        low_value = 1
        high_value = 50
        magic_number = random.randint(low_value, high_value)
        still_guessing = True

        message = ''

    return render_template('index.html', message = message,
        low_value = low_value, high_value = high_value, still_guessing = still_guessing)

if __name__ == '__main__':
    app.run()
