import os
from dotenv import load_dotenv

dotenv_path = f"server_config.env"

load_dotenv(dotenv_path, override=True)


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_CONNECT")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
