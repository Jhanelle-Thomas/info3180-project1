from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def create_profile():
    return render_template('')
    
@app.route('/profiles')
def get_profiles():
    return render_template('')
    
@app.route('/profile/<userid>')
def get_profile():
    return render_template('')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")