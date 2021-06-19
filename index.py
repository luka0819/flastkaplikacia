from cloudipsp import Api, Checkout
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///lukashop.db'
db=SQLAlchemy(app)
#DB-TABLE-RECORDS
#TABLE
#ID TITLE PRICE ISACTIVE
#1 SOME 100 TRUE
#2 SOME 200 FALSE
class Item (db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    price=db.Column(db.Integer, nullable=False)
    isactive=db.Column(db.Boolean,default=True)

@app.route('/')
def index(search = ""):



    items = ["item1", "item2", "itm3", "item4", "item5", "item6", "itm7", "item8"]
    filtered = []
    i = 0
    for item in items:
        i += 33.5
        if search in item:
            filtered.append({"name": item, "price": 10 + i})
    items = Item.query.order_by(Item.price).all()


    return render_template('index.html', items = filtered, warn = ("Nothing found!" if len(filtered) == 0 else ""))


@app.route('/search', methods=['GET'])
def search():
    if request.method == "GET":
        print(request.args)
        search = request.args['search']
        #select from table where text like search

        return index(search)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        #add user to database

        return index()  
    else:  
        return render_template("login.html")

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        #add user to database

        return index()
    else:  
        return render_template("register.html")


@app.route('/buy', methods=['POST'])
def buy():
    if request.method == "POST":
        print(request.form)
        item = request.form['item']

    return index()
@app.route('/create')
@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        item = Item(title=title,price=price)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "შეცდომა მოხდა"
    else:
        return render_template('create.html')
if __name__=="__main__":
   app.run(debug=True)

if __name__=="__main__":
   app.run(debug=True)
