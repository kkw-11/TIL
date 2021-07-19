from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base
from model.user_model import UserModel

engine = create_engine("sqlite:///main.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

@app.route("/signup", methods=["POST"])
def signup():
    """회원가입"""
    # flask request 값 가져오기
    username = request.form.get("username")
    password = request.form.get("password")
    name = request.form.get("name")
    email = request.form.get("email")

    # sqlalchemy를 이용하여 db에 사용자 저장하기
    user = UserModel(username, password, name, email)
    session.add(user)
    session.commit()
    
    return "SUCCESS"


@app.route("/signin", methods=["POST"])
def signin():
    """로그인"""
    # flask request에서 값 가져오기
    username = request.form.get("username")
    password = request.form.get("password")

    # 값으로 db 조회하여 사용자 찾기
    user = session.query(UserModel).filter(
        UserModel.username == username, 
        UserModel.password == password
    ).one_or_none()
    print("hello")
    if user is None:
        return "No User"

    return jsonify({
        "user_id":user.user_id,
        "username":user.username,
        "password": user.password,
        "name": user.name,
        "email" : user.email
    })

app.run(debug=True)
# def change_password(user_id):
#     """비밀번호 변경"""
    
#     pass


# def delete_user():
#     """사용자 탈퇴"""
#     pass
## sql alchemy 이용전
# import sqlite3

# con = sqlite3.connect("main.db")

# cur = con.cursor()

# # cur.execute("CREATE TABLE user (user_id int, username varchar(50), password varchar(50));")
    


# # 데이터 생성
# # cur.execute("INSERT INTO user(user_id, username, password) VALUES(1, 'kim', 'pw');")
# # cur.execute("INSERT INTO user(user_id, username, password) VALUES(2, 'kim', 'pw2');")
# # con.commit()


# #데이터 삭제
# cur.execute("DELETE FROM user where user_id = 1;")
# con.commit()


# ## sqlalchemy 이용
# from model.user_model import UserModel
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from model import Base
# from model.user_model import UserModel

# engine = create_engine("sqlite:///main.db")
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()
# # user = UserModel("username", "1234", "bob", "me@elice.kr")
# # session.add(user)
# # session.commit()

# selected_users = session.query(UserModel).filter(UserModel.name=="bob").all()

# selected_user = session.query(UserModel).filter(UserModel.name=="bob").one_or_none()

# print(selected_users)

# # print(selected_user.user_id, selected_user.username, selected_user.password, selected_user.name, selected_user.email)

# session.delete(selected_user)

# app = None
# @app.route("/users")
# def list_user():
#     users = selected_users = session.query(UserModel).all()

#     return jsonify(users)


