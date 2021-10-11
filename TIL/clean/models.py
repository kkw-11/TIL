from db_connect import db

class Restaurant(db.Model):

    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    restaurant_name = db.Column(db.String(255))
    restaurant_address = db.Column(db.String(255))
    restaurant_phone_number = db.Column(db.String(255))
    hygiene_level = db.Column(db.String(255))
    is_franchise = db.Column(db.Boolean)
    menu = db.Column(db.String(255))
    menu_main_category = db.Column(db.String(255))
    grade = db.Column(db.String(255))
    opening_hours = db.Column(db.String(255))
    holiday = db.Column(db.String(255))


