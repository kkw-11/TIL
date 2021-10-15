from flask import Blueprint, render_template, request, url_for, redirect
from models import *

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def home():
    test_list = cleanTable.query.all()
    return render_template('index.html', test_list = test_list)

@bp.route("/menu")
def hello():
    if request.method == 'GET':
        menu_main_category = request.args.get('input_menu')
        # return menu_main_category
        test_list = cleanTable.query.filter(cleanTable.franchise == 1)
        print(test_list)

        return render_template('index.html', test_list = test_list)

@bp.route("/franchiseList")
def franchiseList():
    if request.method == 'GET':
        # return menu_main_category
        
        test_list = cleanTable.query.filter(cleanTable.franchise == 1)
        print("franchiseList")
        return render_template('index.html', test_list = test_list)

@bp.route("/allList")
def allList():
    if request.method == 'GET':
        # return menu_main_category
        test_list = cleanTable.query.all()
        print("allList")

        return render_template('index.html', test_list = test_list)

