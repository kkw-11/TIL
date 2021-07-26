from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base
from model.user_model import UserModel

engine = create_engine("sqlite:///main.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

app = Flask(__name__)

@app.route("/signup", methods=["POST"])
def signup():
    
    # get values from flask request
    username = request.form.get("username")
    password = request.form.get("password")
    name = request.form.get("name")
    email = request.form.get("email")

    # form - call by postman application
    # args - /url/signup?username=jiyoon&password=pw


    user = UserModel(username, password, name, email)
    session.add(user)
    session.commit()

    return "SUCCESS"

@app.route("/signin", methods=["POST"])
def signin():
    # get values from flask request
    username = request.form.get("username")
    password = request.form.get("password")

    # find user using db value
    user = session.query(UserModel).filter(
        UserModel.username == username, 
        UserModel.password == password
    ).one_or_none()
    if user is None:
        return "No User"
    
    return jsonify({
        "user_id" : user.user_id,
        "username" : user.username,
        "password" : user.password,
        "name" : user.name,
        "email" : user.email
    })

app.run(debug=True)

def change_password(user_id):
    pass

def delete_user():
    pass