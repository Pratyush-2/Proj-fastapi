import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "Pratyush2004"  # <-- replace with your real password
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "nutrition"

    @property
    def database_url(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()
