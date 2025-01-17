from backend.db import create_app

app = create_app()  # создаем экземпляр приложения

if __name__ == "__main__":  # запускаем приложение
    app.run(debug=True)
