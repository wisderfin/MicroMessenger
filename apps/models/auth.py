from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import ModelMixin


class UserModel(ModelMixin):
    __tablename__ = 'user'

    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(60), nullable=False)
