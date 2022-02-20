from app import app
# Flask modules
from flask import render_template, redirect, request, g, session


@app.route('/session/<string:user_name>')
def set_session(user_name):
    session["user_name"] = user_name
    return f"User name {user_name} set to session"

@app.route('/session/<int:dev_route>')
def check_allow(dev_route):
	if dev_route > 0:
		session["allow"] = True
		return "User True set!"
	else:
		session["allow"] = False
		return "User False set!"

@app.route('/session/user')
def get_session():
    return f'>>> {str(session["user_name"])} + {str(session["allow"])}'



@app.after_request
def after_request(res):
	return res