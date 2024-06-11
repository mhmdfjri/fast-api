import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

# Ambil nilai variabel lingkungan untuk koneksi database
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Buat URL koneksi ke database menggunakan nilai variabel lingkungan
url = URL.create(
    drivername="postgresql",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host="db",
    database=POSTGRES_DB,
    port=5432
)

# Buat engine SQLAlchemy
engine = create_engine(url)

# Buat session SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Buat base model SQLAlchemy
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)


Base.metadata.create_all(engine)
