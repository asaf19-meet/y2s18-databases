from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(title, topic, rating):
	new_article = Knowledge(
		title=title,
		topic=topic,
		rating=rating)
	session.add(new_article)
	session.commit()

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(topic=topic).first()
	return article

# def query_article_by_rating(threshold)
	

print(query_all_articles())
print(query_article_by_topic("basketball"))

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

delete_all_articles()
print(query_all_articles())
# print(query_article_by_topic("basketball"))

def edit_article_rating():
	pass

add_article("Basketball", "basketball", 4)
add_article("Taekwondo", "taekwondo", 8)
