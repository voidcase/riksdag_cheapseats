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
    title = pw.CharField(max_length=140)
    body = pw.TextField()
