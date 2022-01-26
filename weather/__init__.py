from flask import Flask
from flask_admin import Admin
app = Flask(__name__)
from weather import routes
app.config['SECRET_KEY']='mysecret'
admin = Admin(app)