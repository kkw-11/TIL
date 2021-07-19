from sqlalchemy import Column, Integer, String, Sequence
from model import Base


class UserModel(Base):
    __tablename__ = "user"

    # By sequence, although I didn't input any value this code add next id on db.
    user_id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    name = Column(String(15))
    email = Column(String(320))


    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email