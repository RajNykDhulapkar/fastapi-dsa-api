from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from .database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50))
    address = Column(String(50))
    phone = Column(String(50))
    posts = relationship("BlogPost", cascade="all, delete")


class BlogPost(Base):
    __tablename__ = "blog_post"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    body = Column(String(200))
    date = Column(Date)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
