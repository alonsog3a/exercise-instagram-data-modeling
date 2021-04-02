import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class USER(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(15)) #15 es el numero max de caracteres
    firstname=Column(String(50))
    lastname=Column(String(50))
    email=Column(String(50))


class POST(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    #street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(USER)

    def to_dict(self):
        return {}

class COMMETS(Base):
    __tablename__ = 'commets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(USER)
    post = relationship(POST)

    def to_dict(self):
        return {}        


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type=Column(String)
    url=Column(String)
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))    
    post = relationship(POST)

    def to_dict(self):
        return {} 


## Draw from SQLAlchemy base
render_er(Base, 'diagram1.png')