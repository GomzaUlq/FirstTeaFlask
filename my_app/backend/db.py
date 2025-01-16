from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DATABASE_URL = "sqlite:///./shop.db"
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from routers.user import user_bp
        from routers.catalog import category_bp, product_bp, main_bp
        from routers.cart import cart_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(category_bp)
        app.register_blueprint(product_bp)
        app.register_blueprint(cart_bp)
        app.register_blueprint(main_bp)

        from models.cart import Cart, CartItem
        from models.user import User
        from models.catalog import Category, Product
        db.create_all()

    return app


