import peewee as pw
from playhouse.db_url import connect
from os import environ
import psycopg2 #token import because pipreqs

db = connect(environ.get('DATABASE_URL') or 'sqlite:///test.db')

class BaseModel(pw.Model):
    class Meta:
        database = db

class Topic(BaseModel):
    # automagic id integer field
    body = pw.TextField()

class Debate(BaseModel):
    id = pw.CharField(primary_key=True)
    title = pw.CharField(max_length=140)
    summary = pw.TextField()

class Speech(Topic):
    person = pw.CharField(max_length=140)
    debate_id = pw.ForeignKeyField(Debate)
    nr = pw.IntegerField()
    party = pw.CharField(max_length=4)
    title = pw.CharField(80)
    body = pw.TextField()

class Annotation(BaseModel):
    # automagic id integer field
    start_index = pw.IntegerField()
    end_index = pw.IntegerField()
    body = pw.TextField()
    parent = pw.ForeignKeyField(Topic, backref='annotations')

class Comment(BaseModel):
    # automagic id integer field
    parent = pw.ForeignKeyField(Annotation, backref='comments')
    body = pw.TextField()

all_tables = [Topic, Debate, Speech, Annotation, Comment]

def reset():
    db.drop_tables(all_tables)
    db.create_tables(all_tables)

def reset_and_populate():
    reset()
    db.drop_tables(all_tables)
    db.create_tables(all_tables)
    t1 = Topic.create(title='Dont drink water', body='Fish fuck in it.')
    t2 = Topic.create(title='SPIDERS!', body='AAAAAAAAAAAAAAAAAAAHHHHHHH!!!!!!!!!!!')
    a1 = Annotation.create(parent=t2, start_index=0, end_index=0, body='Daddy longlegs are not actually spiders')
    c1 = Comment.create(parent=a1, body='They never mentioned Daddy Longlegs')
