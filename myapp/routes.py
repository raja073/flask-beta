from myapp import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Raja'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in kattoor'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The nazis sucks'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)