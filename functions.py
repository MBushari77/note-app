import os
import tempfile
from model import *

def jsonNotes(peweObj):
	notes = []
	for note in peweObj:
		notes.append({'title': note.title, 'content': note.content, 'date': note.date, 'ownerId': note.ownerId, 'id': note.id})
	return notes