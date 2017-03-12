import os, datetime, random, re
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify, make_response
from forms import profileForm
from models import UserProfile
from werkzeug.utils import secure_filename

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile', methods=['GET', 'POST'])
def createProfile():
    form = profileForm()
    
    if request.method == 'GET':
        return render_template('newProfile.html', form=form)
    elif request.method == 'POST':
        imageFolder = app.config['UPLOAD_FOLDER']
        
        if form.validate_on_submit():
            firstname = form.firstname.data
            lastname = form.lastname.data
            age = form.age.data
            gender = form.gender.data
            bio = form.bio.data
            dateCreated = datetime.date.today()
            
            pic = request.files['pic']
            if allowed_file(pic.filename):
                imagename = secure_filename(pic.filename)
                pic.save(os.path.join(imageFolder, imagename))
            
            userid = generateUserId(firstname, lastname)
            username = generateUsername(firstname, lastname)
            
            newUser = UserProfile(userid=userid, username=username, first_name=firstname, last_name=lastname, 
            age=age, gender=gender,biography=bio, pic=imagename, created_on=dateCreated)
                
            db.session.add(newUser)
            db.session.commit()
            
            flash("Profile Successfully Created", "success")
            return redirect(url_for("newProfile"))
    
@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    user
    if request.method == 'GET':
        return render_template('profiles.html')
    elif request.method == 'POST':
        #
    
#@app.route('/profile', methods=['GET', 'POST'])
@app.route('/profile/<userid>', methods=['GET', 'POST'])
def profile(userid):
    if request.method == 'GET':
        return render_template('profile.html',  ,user=user)
    elif request.method == 'POST':
        #
    
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
    
def generateUserId(firstname, lastname):
    temp = re.sub('[.: -]', '', str(datetime.datetime.now()))
    temp = list(temp)
    temp.extend(list(firstname))
    temp.extend(list(lastname))
    random.shuffle(temp)
    return str(temp[:7])
    
def generateUsername(firstname, lastname):
    if len(firstname) <= 5:
        return firstname + str(random.randint(10,1000))
    elif len(lastname) <= 5:
        return lastname + str(random.randint(10,1000))
    else:
        return firstname[:4] + lastname[:4] + str(random.randint(10,100))
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")