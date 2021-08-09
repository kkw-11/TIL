from flask import Flask
from db_connect import db
import config

def create_app():
    app = Flask(__name__)

    app.config.from_object(config) # config 에서 가져온 파일을 사용합니다.

    db.init_app(app)

    from views import main_view
    app.register_blueprint(main_view.bp)

    app.secret_key = "seeeeeeeeeeeecret"
    app.config['SESSION_TYPE'] = 'filesystem'

    return app

if __name__ == "__main__":
    create_app().run(debug=True, port=1234)