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
def profile():
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
            else:
                flash('Incorrect File Format', 'danger')
                return redirect(url_for("profile"))
            
            userid = generateUserId(firstname, lastname)
            username = generateUsername(firstname, lastname)
            
            newUser = UserProfile(userid=userid, username=username, first_name=firstname, last_name=lastname, 
            age=age, gender=gender,biography=bio, pic=imagename, created_on=dateCreated)
                
            db.session.add(newUser)
            db.session.commit()
            
            flash("Profile Successfully Created", "success")
            return redirect(url_for("profile"))
    
@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    user_list = UserProfile.query.all()
    users = [{"username": user.username, "userid": user.userid} for user in user_list]
    
    if request.method == 'GET':
        if user_list is not None:
            return render_template("profiles.html", users=user_list)
        else:
            flash('User Not Found', 'danger')
            return redirect(url_for("home"))
    elif request.method == 'POST':
        if user_list is not None:
            response = make_response(jsonify({"users": users}))                                           
            response.headers['Content-Type'] = 'application/json'            
            return response
        else:
            flash('User Not Found', 'danger')
            return redirect(url_for("home"))

@app.route('/profile/<userid>', methods=['GET', 'POST'])
def viewProfile(userid):
    user = UserProfile.query.filter_by(userid=userid).first()
    
    if request.method == 'GET':
        if user is not None:
            return render_template("profile.html", user=user)
        else:
            flash('User Not Found', 'danger')
            return redirect(url_for("home"))
    elif request.method == 'POST':
        if user is not None:
            response = make_response(jsonify(userid=user.userid, username=user.username, image=user.pic, gender=user.gender, age=user.age,
                    profile_created_on=user.created_on))
            response.headers['Content-Type'] = 'application/json'            
            return response
        else:
            flash('User Not Found', 'danger')
            return redirect(url_for("home"))
    
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
    
def generateUserId(firstname, lastname):
    temp = re.sub('[.: -]', '', str(datetime.datetime.now()))
    temp = list(temp)
    temp.extend(list(map(ord,firstname)))
    temp.extend(list(map(ord,lastname)))
    random.shuffle(temp)
    temp = list(map(str,temp))
    return int("".join(temp[:7]))%10000000
    
def generateUsername(firstname, lastname):
    if len(firstname) <= 5:
        return firstname + str(random.randint(10,1000))
    elif len(lastname) <= 5:
        return lastname + str(random.randint(10,1000))
    else:
        return firstname[:4] + lastname[:4] + str(random.randint(10,100))
    
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")