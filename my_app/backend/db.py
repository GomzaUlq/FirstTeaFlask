from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DATABASE_URL = "sqlite:///./shop.db"
db = SQLAlchemy()  # Экземпляр для работы с бд
migrate = Migrate()  # Экземляр для управления с миграциями


def create_app():  # функция, которая создает и настраивает экземпляр приложения
    app = Flask(__name__, template_folder='../templates', static_folder='../static')  # Создаем экземпляр приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL  # подключение к бд
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # отключение отслеживания изменений объектов
    app.secret_key = "148u1hufw9h2r"  # ключ для защиты сессий

    db.init_app(app)  # инициализация приложения с бд
    migrate.init_app(app, db, command='migrate')  # инициализация приложения, бд с миграциями приложения

    with app.app_context():  # контекст приложения для доступа к объекатам приложения и бд
        from routers.user import user_bp
        from routers.catalog import category_bp, product_bp, main_bp, about_bp, states_bp
        from routers.cart import cart_bp

        app.register_blueprint(user_bp)  # Регистрация всех импортированных маршрутов
        app.register_blueprint(category_bp)
        app.register_blueprint(product_bp)
        app.register_blueprint(cart_bp)
        app.register_blueprint(main_bp)
        app.register_blueprint(about_bp)
        app.register_blueprint(states_bp)

        from models.cart import Cart, CartItem  # Импорт моделей
        from models.user import User
        from models.catalog import Category, Product
        db.create_all()  # Создание таблиц в БД на основе моделей

    return app  # возвращаем приложение
