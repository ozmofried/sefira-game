from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)


app.config["SECRET_KEY"]="hlfndjngonearojvn2v156df4b65zx51vfsz1d5v156"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"


from sefira_counter_game import routes 

