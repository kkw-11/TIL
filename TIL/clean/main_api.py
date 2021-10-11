from flask import Blueprint, render_template, request, url_for, redirect
from models import *

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home():
    test_list = Restaurant.query.all()
    return render_template('index.html', test_list = test_list)

@bp.route("/menu")
def hello():
    if request.method == 'GET':
        menu_main_category = request.args.get('input_menu')
        # return menu_main_category
        test_list = Restaurant.query.filter(Restaurant.menu_main_category.like(f"%{menu_main_category}%")).order_by(Restaurant.grade)
        print(test_list)

        return render_template('index.html', test_list = test_list)


