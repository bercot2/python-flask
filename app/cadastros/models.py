from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.core.models.base_model import BaseModel


class Usuario(BaseModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
