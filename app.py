from flask import Flask, render_template, request
import random

app = Flask(__name__)



names = ["John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava", "Elijah", "Isabella"]

# @app.route('/')
# def index():
#     return render_template('index.html')


def generate_random_names(num_names):
    random_names = random.sample(names, num_names)
    return random_names


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_names = int(request.form['num_names'])
        names = generate_random_names(num_names)
        return render_template('index.html', names=names)
    return render_template('index.html')
