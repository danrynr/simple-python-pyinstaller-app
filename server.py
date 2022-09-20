from flask import flask

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')
    