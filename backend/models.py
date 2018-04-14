import peewee as pw
from playhouse.db_url import connect
from os import environ
import psycopg2 #token import because pipreqs
import datetime

db = connect(environ.get('DATABASE_URL') or 'sqlite:///test.db')

class BaseModel(pw.Model):
    class Meta:
        database = db

class Topic(BaseModel):
    # automagic id integer field
    title = pw.CharField(max_length=140)
    body = pw.TextField()


class Motions(BaseModel):
    title = pw.CharField(max_length=140)
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
    body = pw.TextField()


class Annotation(BaseModel):
    # automagic id integer field
    start_index = pw.IntegerField()
    end_index = pw.IntegerField()
    start_paragraph = pw.IntegerField()
    end_paragraph = pw.IntegerField()
    body = pw.TextField()
    parent = pw.ForeignKeyField(Topic, backref='annotations')
    timestamp = pw.DateTimeField(default=datetime.datetime.now)
    deltas = pw.IntegerField(default=0)


class Comment(BaseModel):
    # automagic id integer field
    parent = pw.ForeignKeyField(Annotation, backref='comments')
    timestamp = pw.DateTimeField(default=datetime.datetime.now)
    body = pw.TextField()
    deltas = pw.IntegerField(default=0)

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
    a1 = Annotation.create(
            parent=t2, 
            start_index=0, 
            end_index=0, 
            start_paragraph=0, 
            end_paragraph=0, 
            body='Daddy longlegs are not actually spiders', 
            )
    c1 = Comment.create(parent=a1, body='They never mentioned Daddy Longlegs', deltas=0)

#     m1 = open("mock/m1", "r").read()
#     m1t = open("mock/m1t", "r").read()

#     m2 = open("mock/m2", "r").read()
#     m2t = open("mock/m2t", "r").read()

#     m3 = open("mock/m3", "r").read()
#     m3t = open("mock/m3t", "r").read()

#     Motions.create(title=m1t, text=m1)
#     Motions.create(title=m2t, text=m2)
#     Motions.create(title=m3t, text=m3)





