from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index= True)
    uid = Column(String)
    username = Column(String)
    email = Column(String)
    provider = Column(String)
    avatar = Column(String)
    nickname = Column(String)
    verified = Column(Boolean)
    onboarded = Column(Boolean)
    created_at = Column(String)
    last_logged_in = Column(String)

