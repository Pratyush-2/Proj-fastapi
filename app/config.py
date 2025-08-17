"""Configuration for the application."""
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Settings for the application."""
    # pylint: disable=too-few-public-methods
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "Pratyush2004"  # <-- replace with your real password
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "nutrition"

    @property
    def database_url(self):
        """Returns the database URL."""
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()
