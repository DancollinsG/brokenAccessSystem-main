
from flask import *
import pymysql

# create a Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signin')
def login():
    return render_template('signin.html')

app.run(debug=True)