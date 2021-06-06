from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.jinja')

@app.route('/html')
def html_hints():
    return render_template('html-hints.jinja')

@app.route('/css')
def css_hints():
    return render_template('css-hints.jinja')

@app.route('/js')
def js_hints():
    return render_template('js-hints.jinja')
