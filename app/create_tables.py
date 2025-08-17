"""Creates the tables in the database."""

from .database import engine, Base

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
