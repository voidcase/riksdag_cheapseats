import peewee as pw
from playhouse.db_url import connect
from os import environ

db = connect(environ.get('DATABASE_URL') or 'sqlite:///test.db')
class BaseModel(pw.Model):
    class Meta:
        database = db

class Topic(BaseModel):
    # automagic id integer field
    title = pw.CharField(80)
    body = pw.TextField()

class Annotation(BaseModel):
    # automagic id integer field
    start_index = pw.IntegerField()
    end_index = pw.IntegerField()
    body = pw.TextField()
    parent = pw.ForeignKeyField(Topic, backref='annotations')
