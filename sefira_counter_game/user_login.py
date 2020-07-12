from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from sefira_counter_game.dbmodels import User  

class SignupForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo('password')])
    submit_button = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            return ValidationError(), flash('Username already taken. Please choose another one.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return ValidationError(),flash('Email has  already been signed up.')   


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit_button = SubmitField("Login")
