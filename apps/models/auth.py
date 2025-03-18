from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from models.base import ModelMixin


class UserModel(ModelMixin):
    __tablename__ = 'user'

    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(60), nullable=False)

    refresh_tokens: Mapped[list['JWTRefreshModel']] = relationship(
        'JWTRefreshModel',
        back_populates='user'
    )


class JWTRefreshModel(ModelMixin):
    __tablename__ = 'jwt_refresh'

    user_uuid: Mapped[UUID] = mapped_column(
        UUID, ForeignKey('user.uuid'), nullable=False
    )
    refresh_tokens: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped[UserModel] = relationship('UserModel', back_populates='refresh_tokens')
