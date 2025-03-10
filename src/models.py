import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250), nullable=False)
    email = Column(String(250))
    follower = relationship('Follower')

class Coment(Base):
    __tablename__ = 'coment'
    id = Column(Integer, primary_key=True)
    coment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship('User')

class Post(Base):
    __tablename__ = 'post'    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    coment = relationship("Coment")
    user = relationship('User')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum("imagen", "gif", "video"))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship('Post')

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))
    user = relationship('User')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e