from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from app.backend.models import Base
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(64))
    first_name = mapped_column(String(30))
    email = mapped_column(String(120))
    password_hash = mapped_column(String(128))
    slug = mapped_column(String, unique=True, index=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
