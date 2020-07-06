from flask import Flask, render_template, request, redirect, url_for, session, jsonify, make_response
import datetime
from model import *
from functions import *
# import os
# import json

# import runpy

# initializing flask
app = Flask(__name__)
app.secret_key = os.urandom(24)


# LOGIN PAGE ROUTE
@app.route('/')
def index():
	try:
		if session['status'] == "logedIn":
			return "loged in"
	except KeyError:
		return render_template('index.html')


# login page
@app.route('/login')
def login():
	try:
		print(session['userId'])
		return redirect(url_for('notes'))
	except KeyError:
		return render_template('login.html')

# LOGIN PAGE ROUTE
@app.route('/logining', methods=['GET', 'POST'])
def logining():
	try:
		if request.method == 'POST':
			name = request.form['username']
			password = request.form['password']
			for user in User.select():
				if (user.name == name) & (user.password == password):
					session['status'] = 'logedIn'
					session['userId'] = user.id
					print(user.id)
					return redirect(url_for('notes'))
			return render_template('login.html')
		else:
			return redirect(url_for('login.html'))
	except KeyError:
		return render_template('login.html')





# register page
@app.route('/register')
def register():
	return render_template('register.html')

# ADD NEW USER
@app.route('/registering', methods=['GET', 'POST'])
def registering():
	if request.method == 'POST':
		if request.form['password'] == request.form['passwordConfirm']:
			User.create(
				name = request.form['username'],
				password = request.form['password']
			)
			return "registered"
		else:
			# return redirect(url_for('index'))
			return "password doesnt match"
	# redirect to show all users page
	return redirect(url_for('allusers'))


# show all notes
@app.route('/notes')
def notes():
	try:
		notes = jsonNotes(Notes.select().where(Notes.ownerId == session['userId']))
		notes.reverse()
		print(notes)
		return render_template('notes.html', notes=notes)
	except KeyError:
		return redirect(url_for('login'))



# save a note
@app.route('/savenote', methods=['GET', 'POST'])
def savenote():
	if request.method == 'POST':
		Notes.create(
			title = request.form['title'],
			content = request.form['content'],
			ownerId = int(session['userId'])
		)
	return redirect(url_for('notes'))


# show one notes
@app.route('/note/<int:id>')
def note(id):
	try:
		note = jsonNotes(Notes.select().where((Notes.ownerId == session['userId']) & (Notes.id == id)))
		return render_template('note.html', note=note)
	except KeyError:
		return redirect(url_for('login'))

# add new note
@app.route('/newnote')
def newnote():
	try:
		print(session['userId'])
		return render_template('newnote.html')
	except KeyError:
		return redirect(url_for('login'))

# delete note
@app.route('/delete/<int:id>')
def deleteNote(id):
	try:
		print(session['userId'])
		Notes.delete().where(Notes.id == id).execute()
		return redirect(url_for('notes'))
	except KeyError:
		return redirect(url_for('login'))

# edit note
@app.route('/edit/<int:id>')
def edit(id):
	try:
		note = jsonNotes(Notes.select().where((Notes.ownerId == session['userId']) & (Notes.id == id)))
		return render_template('editnote.html', note=note)
	except KeyError:
		return redirect(url_for('login'))


@app.route('/editnote/<int:id>', methods=['GET', 'POST'])
def editnote(id):
	try:
		if request.method == 'POST':
			note = 0 
			for n in Notes.select().where((Notes.ownerId == session['userId']) & (Notes.id == id)):
				note = n
			note.get()
			note.title = request.form['title']
			note.content = request.form['content']
			note.save()
			return redirect(url_for('notes'))
	except KeyError:
		return redirect(url_for('login'))



if __name__ == '__main__':
	app.run(debug=True)

