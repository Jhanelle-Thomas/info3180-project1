from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "fb9ks45XCLewDFL15"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:pass@localhost/proj"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
