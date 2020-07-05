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
	return render_template('login.html')

# LOGIN PAGE ROUTE
@app.route('/logining', methods=['GET', 'POST'])
def logining():
	if request.method == 'POST':
		name = request.form['username']
		password = request.form['password']
		for user in User.select():
			if (user.name == name) & (user.password == password):
				session['status'] = 'logedIn'
				session['userId'] = user.id
				print(user.id)
				return "done"
		return 'not found'





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
	return render_template('notes.html')



# show one notes
@app.route('/note')
def note():
	return render_template('note.html')

# add new note
@app.route('/newnote')
def newnote():
	return render_template('newnote.html')


if __name__ == '__main__':
	app.run(debug=True)

