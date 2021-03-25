import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(30))
    first_name = Column(String(30))
    second_name = Column(String(30))
    password = Column(String(30))
    password_confirmation = Column(String(30))
    state = Column(Boolean, default=True)


class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250))
    email = Column(String(250))
    phone = Column(String(250), nullable=False)
    state = Column(Integer, ForeignKey('login.state'))
    username = Column(Integer, ForeignKey('login.username'))
    password = Column(Integer, ForeignKey('login.password'))
    login = relationship(login)

class likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    n_likes = Column(Integer)
    username = Column(String(250))
    nickname = Column(String(250))
    post_id = Column(Integer, ForeignKey("post.id"))
    follow = Column(Boolean, default=True)

class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    photo = Column(String(250))
    video = Column(String(250))
    url = Column(String(250))
    text = Column(String(250))
    comments = Column(String(250))
    n_likes = Column(Integer)
    likes = relationship(likes)

class feed(Base):
    __tablename__ = 'feed'
    id = Column(Integer, primary_key=True)
    n_posts = Column(String(250))
    followers = Column(String(250))
    post_id = Column(Integer, ForeignKey("post.id"))
    user =relationship(user)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')