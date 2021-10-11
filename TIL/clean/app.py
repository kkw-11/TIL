from flask import Flask
from db_connect import db
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    import main_api
    app.register_blueprint(main_api.bp)

    return app
    
if __name__ == "__main__":
    create_app().run(debug=True, port=1234)
