from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

secret_number = None
max_guesses = 5

@app.route('/')
def start_game():
    global guesses_left, secret_number 
    guesses_left = max_guesses  
    secret_number = random.randint(1, 100)  
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess_number():
    global secret_number, guesses_left
    guess = int(request.form['guess'])

    guesses_left -= 1  

    if guess == secret_number:
        return redirect(url_for('win'))
    
    elif guesses_left > 0:
        if guess < secret_number:
            return render_template('index.html', message="Too low!", guesses_left=guesses_left)
        else:
            return render_template('index.html', message="Too high!", guesses_left=guesses_left)
    else:
        return render_template('game_over.html', secret_number=secret_number)

@app.route('/win')
def win():
    return render_template('win.html')

if __name__ == '__main__':
    app.run(debug=True)
