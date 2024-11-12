from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Sai Balaji</p>"

@app.route('/login')
def login():
    return "loginpage"

@app.route("/register")
def register():
    return "register"

@app.route("/index")
def index():
    return "index" 

#dynamic routing
#string route (default type)
@app.route('/user/<string:username>')
def show_user(username):
    return f"Hello,{username}"

@app.route('/id/<int:id>')
def show_id(id):
    return f"Vennela,{id}"

@app.route('/price/<float:price>')
def show_price(price):
    return f'The price is {price}'

@app.route('/path/<path:subpath>')
def show_path(subpath):
    return f'The path is {subpath}'          

app.run()