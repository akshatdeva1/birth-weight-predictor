
#import flask , jsonify
from flask import Flask, jsonify, render_template

#create flask instance
app = Flask(__name__)

#define function and route
# '/', '/about', '/data'

#@app.route('/')
#def home():
   # return "Welcome to my website!"

@app.route('/about') 
def about():
    return """<h1>About Me:</h1><br>
          <h2>My name is Akshat Deva.</h2><br>
          <h3>I am a software developer with a passion for learning new technologies.</h3>"""

@app.route('/data')
def data():
    user_data = {"name": "", "age": 28}
    return jsonify(user_data)

#@app.route('/')
#def home_page():
   # name= "Akshat Deva"
   # return render_template('index.html', name=name)

#@app.route('/', methods=['GET'])
#def home():
   # return "Hello World!"

@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def welcome():
    return "We have received your information"

#trigger the flask app
if __name__ == "__main__":
    app.run(debug=True)