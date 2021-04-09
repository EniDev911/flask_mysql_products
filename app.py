#-------------------------------------------------------------------------------
# Author:      Enidev
#
# Created:     09-04-2021
# Copyright:   (c) Enidev 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/student')
def student():
	return 'Students page'

@app.route('/user/<name>')
def user(name):
	if name == 'home':
		return redirect(url_for('index'))
	if name == 'student':
		return redirect(url_for('student'))
	if name == 'quewea':
		return redirect(url_for('student'))


if __name__ == '__main__':
    app.run(debug = True, port = 4000)
