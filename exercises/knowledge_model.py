from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__='Knowledge'

	id_number = Column(Integer, primary_key=True)
	title = Column(String)
	topic = Column(String)
	rating = Column(Integer)
	def __repr__(self):
		return(
			"id number: {}\n"
			"article title: {}\n"
			"article topic: {}\n"
			"article rating: {}").format(
			self.id_number, self.title, self.topic, self.rating)



