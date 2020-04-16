from flask import render_template, request,flash, redirect, url_for,session
from app import app
@app.route('/')
def sample():
	return render_template("index.html")
