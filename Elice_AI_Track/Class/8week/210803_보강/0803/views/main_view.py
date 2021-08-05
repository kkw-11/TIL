from flask import Blueprint, render_template, request, url_for, session, flash, redirect
from models import *
# from bcrypt import hashpw, checkpw, gensalt
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('main', __name__, url_prefix='/')

# 메인 페이지입니다!
# 가게의 정보를 가져와서 띄워봅시다.
#
@bp.route('/')
def home():
    store_list = rabbitStore.query.order_by(rabbitStore.name.asc())
    return render_template('main.html', store_list=store_list)

# 가게의 정보를 출력하기 위한 부분이에요.
@bp.route('/store/<int:store_id>/')
def store_detail(store_id):
    store_info = rabbitStore.query.filter(rabbitStore.id == store_id).first()

    return render_template('store_detail.html', store_info = store_info)


# 로그인 아주 중요하죠.
# 잘 생각해봅시다!
@bp.route('/login', methods=('POST', 'GET'))
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    id = request.form['user_id']
    password = request.form['password']

    user_data = rabbitUser.query.filter(rabbitUser.id == id).first()

    if not user_data:
        flash("존재하지 않는 아이디 입니다.")
        return redirect('/login')
    
    if not check_password_hash(user_data.password, password):
        flash("비밀번호가 틀립니다.")
        return redirect(url_for('main.login'))

    session.clear()
    session['user_id'] = id
    session['nickname'] = user_data.nickname

    flash(f"안녕하세요 , {user_data.nickname}님!")
    return redirect('/')


# 로그아웃입니다.
# 세션만 날려주시죠!
@bp.route('/logout')
def logout():
    session.clear()
    flash("안녕히가세요!")
    return redirect(url_for('main.home'))

# 회원가입입니다.
# 일반적인 사이트의 회원가입 절차를 잘 생각해보세요.
# hashpw을 왜 사용하는지, gensalt는 왜 있는지 생각해보세요.
@bp.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'GET':
        return render_template('register.html')

    # 회원가입 -> 폼에 있는 정보를 가져와야 함.
    username    = request.form['user_id']
    password    = request.form['password']
    nickname    = request.form['nickname']
    telephone   = request.form['telephone']

    user_info = rabbitUser.query.filter(rabbitUser.id == username).first()
    if user_info:
        flash("이미 가입된 아이디입니다.")
        return redirect('/register')

    password = generate_password_hash(password)
    user = rabbitUser(id=username, password=password, nickname=nickname, telephone=telephone)
    db.session.add(user)
    db.session.commit()

    flash("회원가입이 완료되었습니다. 로그인 해주세요.")
    return redirect('/')

# 리뷰 작성입니다.
# user_id, store_id, 나머지 두개을 어떤 식으로 받는지 잘 체크하세요.
@bp.route('/write_review/<int:store_id>/', methods=('POST',))
def create_review(store_id):
    pass

# 리뷰 삭제입니다.
# 리뷰 삭제를 위해선 일단 이 리뷰가 해당 유저가 쓴게 맞는지,
# 이 리뷰가 그 가게의 리뷰가 맞는지 확인해야 합니다.
@bp.route('/delete_review/<int:store_id>/<int:review_id>')
def delete_review(store_id, review_id):
    pass

# 마이 페이지라고 써있지만, 사실 그냥 개인정보 수정용이에요!
# 다만, 로그인을 한 유저만 접근할 수 있도록 해야겠죠?
@bp.route('/mypage', methods=('POST', 'GET'))
def update_info():
    pass