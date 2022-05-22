# SQLAlchemy import
from sqlalchemy import String, Integer, Boolean, DATETIME, Column,  event
from tasks import Base

# SQLAlchemy table
class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(30))
    pages = Column(String(30))
    hw_detail = Column(String(124))
    modify_time = Column(DATETIME)
    reminding_time = Column(String(30))
    reminding_date = Column(String(30))
    done = Column(Boolean)
