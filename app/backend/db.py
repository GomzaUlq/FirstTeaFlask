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
        from app.routers.user import user_bp
        from app.routers.catalog import category_bp, product_bp, main_bp
        from app.routers.cart import cart_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(category_bp)
        app.register_blueprint(product_bp)
        app.register_blueprint(cart_bp)
        app.register_blueprint(main_bp)

        from app.models.cart import Cart, CartItem
        from app.models.user import User
        from app.models.catalog import Category, Product
        db.create_all()

    return app
