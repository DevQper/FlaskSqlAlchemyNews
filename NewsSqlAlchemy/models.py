from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session
from flask import Flask


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0000@localhost/News'    
db = SQLAlchemy(app)

""" News Model """

class News(db.Model):
    __tablename__ = 'News'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    overview = db.Column('overview', db.String)
    link = db.Column('link', db.String)
    paragraphs = db.Column('paragraphs', db.Text)

    def __init__(self, id, title, overview, link, paragraphs):
        self.id = id
        self.title = title
        self.overview = overview
        self.link = link
        self.paragraphs = paragraphs
    
    
    def find_id():
        news = News.query.all()
        return len(news)
        
def add_news_to_db(new_title, new_overview, new_link, new_paragraphs):
        
        news = News(News.find_id()+1, new_title, new_overview, new_link, new_paragraphs)
        db.session.add(news)
        db.session.commit()

def get_the_news():
        news = News.query.all()   
        news = news[-10:]
        return news
        

""" Use this command to implement the database 1 time"""
# db.create_all()

# print(News.find_id())
# News.add_news_to_db("cordana to the moon", 'Cordanatothemoon', 'mooon', 'dsadasdadada')

    