import peewee as pw
from playhouse.db_url import connect
from os import environ
import psycopg2

db = connect(environ.get('DATABASE_URL') or 'sqlite:///test.db')

class BaseModel(pw.Model):
    class Meta:
        database = db

class Document(BaseModel):
    # automagic id integer field
    body = pw.TextField()

class Debate(BaseModel):
    id = pw.CharField(primary_key=True)
    title = pw.CharField(max_length=140)
    summary = pw.TextField()

class Speech(Document):
    person = pw.CharField(max_length=140)
    debate_id = pw.ForeignKeyField(Debate)
    nr = pw.IntegerField()
    party = pw.CharField(max_length=4)
