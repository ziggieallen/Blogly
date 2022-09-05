from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Homepage redirects to list of users"""

    return redirect("/users")

@app.route('/users')
def users_index():
    """Show a page with info on all users"""

    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template("index.html", users=users)

@app.route('/users/new', methods=["GET"])   
def add_user():
    """Show a form to create new user"""

    return render_template("add-user.html") 

@app.route('/users/new', methods=["POST"])
def create_user():
    """Handle form submission for creating a new user"""

    first_name = request.form["first-name"]   
    last_name = request.form["last-name"] 
    img = request.form["img"]   

    new_user = User(first_name=first_name, last_name=last_name, image_url=img) 

    db.session.add(new_user)
    db.session.commit()    

    return redirect("/users")

@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show a page with info on a specific user"""

    user = User.query.get_or_404(user_id)
    # Gives us a pk and the id that were using in the url should match the id col (pk) 
    # in pets table
    return render_template("detail.html", user=user)   

@app.route('/users/<int:user_id>/edit')
def users_edit(user_id):
    """Show a form to edit an existing user"""

    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)     

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")    

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")    
