from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    return render_template('search.html')

# pwa
@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('js/sw.js')
