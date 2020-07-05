from peewee import *
import datetime
import json


db = SqliteDatabase('p_database.db')
# PRODUCTS TABLE
class User(Model):
	name = CharField()
	password = CharField()
	notes = IntegerField(default=0)
	 # = IntegerField()

	class Meta:
		database = db

# PRODUCTS TABLE
class Notes(Model):
	title = CharField()
	content = CharField()
	date = CharField(default=str(datetime.datetime.now())[0:16])
	ownerId = IntegerField()
	 # = IntegerField()

	class Meta:
		database = db



# initialize the database
def initialize_db():
	db.connect()
	db.create_tables([User, Notes], safe = True)

initialize_db()

# User.create(username="admin", password="admin", userType="admin")