# from urllib import request

from Portfolio import app
from flask import render_template, request, redirect


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/components')
def components():
    return render_template('components.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        # print(request)
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        with open("database.txt", 'a') as f:
            f.write(f"{email},{subject},{message}\n")

        return redirect('/thanks.html')
