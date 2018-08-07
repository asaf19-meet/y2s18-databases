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
			"if you want to learn about {}\n"
			"you should go to wikipedia and search for {}\n"
			"the rating that we gave it is {} out of 10\n").format(
			self.id_number, self.topic, self.title, self.rating)



