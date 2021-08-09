from flask import Blueprint, render_template, request, url_for, session, flash, redirect, jsonify
from models import *
# from bcrypt import hashpw, checkpw, gensalt
from werkzeug.security import generate_password_hash, check_password_hash
import requests

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
    store_menu = rabbitMenu.query.filter(rabbitMenu.store_id == store_id).all()
    reviews = rabbitReview.query.filter(rabbitReview.store_id == store_id).all()

    return render_template('store_detail.html', store_info = store_info, store_menu=store_menu, review_info=reviews)


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
    rating = int(request.form['star'])
    content = request.form['review']

    review = rabbitReview(user_id =session['user_id'], store_id = store_id, rating=rating, content=content)
    db.session.add(review)
    db.session.commit()

    flash("리뷰가 성공적으로 작성되었습니다.")
    return redirect(f'/store/{store_id}')
    # return redirect(url_for('main.store_detail',store_id= store_id))


# 리뷰 삭제입니다.
# 리뷰 삭제를 위해선 일단 이 리뷰가 해당 유저가 쓴게 맞는지,
# 이 리뷰가 그 가게의 리뷰가 맞는지 확인해야 합니다.
@bp.route('/delete_review/<int:store_id>/<int:review_id>')
def delete_review(store_id, review_id):
    review_info = rabbitReview.query.filter(rabbitReview.id == review_id).first()
    store_info = rabbitStore.query.filter(rabbitStore.id == store_id).first()

    if review_info.user_id != session['user_id']:
        flash("삭제할 권한이 없습니다.")
    elif review_info.store_id != store_info.id:
        flash("잘못된 요청입니다.")
    else:
        db.session.delete(review_info)
        db.session.commit()
        flash("삭제가 완료되었습니다.")
        
        

# 마이 페이지라고 써있지만, 사실 그냥 개인정보 수정용이에요!
# 다만, 로그인을 한 유저만 접근할 수 있도록 해야겠죠?
@bp.route('/mypage', methods=('POST', 'GET'))
def update_info():
    pass


@bp.route('/kakao')
def kakao_login():
    client_id = 'fe8afea007be64a298c41c191f0e5daa'
    redirect_uri = 'http://localhost:1234/kakao/callback'
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")

@bp.route('/kakao/callback')
def kakao_login_process():
    code = request.args.get("code")
    client_id = 'fe8afea007be64a298c41c191f0e5daa'
    redirect_uri = 'http://localhost:1234/kakao/callback'

    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
    )

    token_json = token_request.json() # 돌아온 결과물에서 json 데이터만 빼온다
    print(token_json)

    access_token = token_json.get("access_token")

    # 이 토큰이 제대로 된 토큰이 맞는지 카카오에게 검증을 해보자
    profile_request = requests.get(
    "https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"},)


    profile_json = profile_request.json()

    kakao_account = profile_json.get("kakao_account")
    email = kakao_account.get("email", None)
    kakao_id = profile_json.get("id")



    session['user_id'] = kakao_id
    session['nickname'] = kakao_account['profile']['nickname']

    return redirect('/')

