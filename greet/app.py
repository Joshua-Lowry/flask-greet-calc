from flask import Flask, request
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    print("welcome")
    html = """
    <h1>welcome</h1>
    """
    return html

@app.route('/welcome/home')
def welcome_home():
    print("welcome home")
    html = """
    <h1>welcome home</h1>
    """
    return html

@app.route('/welcome/back')
def welcome_back():
    print("welcome back")
    html = """
    <h1>welcome back</h1>
    """
    return html
