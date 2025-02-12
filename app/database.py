from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# PostgreSQL Database URL

DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/finance_tracker"

# Create Engine
engine = create_engine(DATABASE_URL)

# try:
#     with engine.connect() as conn:
#         print("✅ Connected successfully!")
# except Exception as e:
#     print(f"❌ Connection failed: {e}")

# Session Local Class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Class for ORM models
Base = declarative_base()

# Dependency for DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()