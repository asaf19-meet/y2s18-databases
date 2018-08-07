from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating):
	new_article = Knowledge(
		topic=topic,
		title=title,
		rating=rating)
	session.add(new_article)
	session.commit()

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

def query_article_by_topic(topic):
	article = session.query(
		Knowledge).filter_by(
		topic=topic).first()
	return article

def query_article_by_rating(threshold):
	articles = query_all_articles()
	list_lower_then_threshold = []
	for i in articles:
		if i.rating<threshold:
			list_lower_then_threshold.append(i)
	return list_lower_then_threshold

def query_article_by_primary_key(id_number):
	article = session.query(
		Knowledge).filter_by(
		id_number = id_number).first()
	return article
	

def delete_article_by_topic(topic):
	session.query(
		Knowledge).filter_by(
		topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()


# print(query_article_by_topic("basketball"))

def edit_article_rating(article_title, update_rating):
	article_object = session.query(
		Knowledge).filter_by(
		title = article_title).first()
	article_object.rating = update_rating
	session.commit()
	

def top_5_rating():
	articles = query_all_articles()
	top_5 = [articles(0),articles(1),articles(2),articles(3),articles(4)]
	for i in articles:
		for x in top_5:
			if i.rating>x.rating:
				top_5.index(x) = i	
	return top_5	
		









# add_article("martial arts", "taekwondo", 8)
# print(query_all_articles())
# edit_article_rating("basketball", 9)
# print(query_all_articles())
# delete_all_articles()