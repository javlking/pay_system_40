from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:admin@localhost/pay_system')
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# генератор соединений
def get_db():
    db = SessionLocal()

    try:
        yield db
    except:
        db.rollback()
        return
    finally:
        db.close()

from database import models


