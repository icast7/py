from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Miguel'} #a user
	posts = [#example posts
		{
			'author': {'nickname': 'John'},
			'body': 'Beautiful day in PDX!'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'The avengers movie was cool!'
		}
	]
	return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form = form)