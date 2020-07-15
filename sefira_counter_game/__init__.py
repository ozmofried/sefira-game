from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)


app.config["SECRET_KEY"]="hlfndjngonearojvn2v156df4b65zx51vfsz1d5v156"
app.config['SQLALCHEMY_DATABASE_URL'] = ' postgres://gnrjraqdoihaxs:c637b97f64b3e7317638d8afc41f354c16738541ff4335978fc2d3c80909ccad@ec2-54-211-210-149.compute-1.amazonaws.com:5432/d61kpbpku9upil'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"


from sefira_counter_game import routes 

