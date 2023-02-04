from flask import Flask, render_template

import backend, pantry

app = Flask(__name__)

@app.route('/')
def index():
    print("Request for index page received.")
    return render_template('index.html')


@app.route('/pantry')
def pantry_page():
    print("Request for index page received.")
    return render_template('index.html', pantry_items=pantry.foods)

if __name__ == '__main__':
   app.run()