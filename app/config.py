from pathlib import Path

class Settings:
    DB_FILE = Path(__file__).parent / "nutrition_app.db"

    @property
    def database_url(self):
        return f"sqlite:///{self.DB_FILE}"

settings = Settings()
