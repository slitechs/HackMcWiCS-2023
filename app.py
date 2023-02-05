from flask import Flask, render_template, request, redirect, url_for, send_from_directory

import os
from werkzeug.utils import secure_filename

# Imports for funcionality
import backend, pantry, search


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home page
@app.route('/')
def index():
    print("Request for index page received.")
    return render_template('index.html')

# For uploading images

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('pantry.html', pantry_items=pantry.get_items(filename))
        else:
            return "File type not supported."

    return render_template('upload.html')


# Pantry page
@app.route('/pantry')
def pantry_page():
    print("Request for index page received.")
    return render_template('pantry.html', pantry_items=pantry.foods)

# Recipe page (redirects to web search)
@app.route('/recipes', methods=['GET', 'POST'])
def get_recipe():
    if request.method == 'POST':
        search_term = request.form['text']
        
        search.search_web(search_term)
        

    return render_template('recipe.html')

if __name__ == '__main__':
   app.run()