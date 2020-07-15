from sefira_counter_game.user_login import LoginForm, SignupForm 
from sefira_counter_game import sefira_game2
from flask import Flask, render_template, request, redirect, flash, url_for, session  
from sefira_counter_game import app, db
from sefira_counter_game.dbmodels import User, Score  
from flask_login import login_user, current_user, logout_user, login_required




@app.route('/login',methods=["POST", "GET"])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    
    if request.method == "POST":
        user = User.query.filter_by(email=email).first()
        if user:
            user_pass = user.password
            if user_pass == password:
                login_user(user)
                flash(f"{user.username} Logged In")
                session['score'] = 0
                num_and_day = sefira_game2.number_picker()
                num = num_and_day[0]
                day = num_and_day[1] 
                session['num'] = num
                session['day'] = day
                session['message']= 'Please enter number above'
                return redirect(url_for("game"))
        else:
            flash("Login unsuccessful. Please try again.")
    return render_template ('login.html', title="Login", form=form)  


@app.route('/', methods=["POST", "GET"])
@login_required
def game():
    print(session['message'])
    score = session['score']
    print(score)
    guess = request.form.get("input_field")    
    
    if request.method == "POST":
        if int(guess) == session['num']:
            session['score']  = session['score'] + 1
            session['message'] = "Well Done"
            num_and_day = sefira_game2.number_picker()
            num = num_and_day[0]
            day = num_and_day[1] 
            session['num'] = num
            session['day'] = day
        else:
            session['score']  = session['score'] - 1
            session['message'] = "Try again!"  
        return render_template("sefiracounter.html",score=session['score'], day=session['day'], n=session['message'])
    
    else:
        return render_template("sefiracounter.html",score=session['score'] , day=session['day'], n=session['message'])



@app.route('/timed_out', methods=["POST","GET"])
@login_required
def timed_out():
    session['score']  = session['score'] - 1
    session['message'] = "Timed Out... Next!"
    num_and_day = sefira_game2.number_picker()
    num = num_and_day[0]
    day = num_and_day[1] 
    session['num'] = num
    session['day'] = day
    
    return redirect(url_for("game"))


@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    form = SignupForm()

    if form.validate_on_submit() and not form.validate_username(form.username) and not form.validate_email(form.email):
        flash("All Signed Up,\n Let's Play!!")
        new_user=User(username = form.username.data, email= form.email.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("game"))
    else:    
        return render_template ('sign_up.html', title="Sign Up", form=form)


@app.route('/rules')
def the_rules():
    return render_template("rules.html") 


@app.route('/logout')
def logout():
    game_score = Score(score= session['score'], player= current_user) 
    db.session.add(game_score)
    db.session.commit()
    logout_user()
    return redirect(url_for("login"))


@app.route('/user_page')
def user_page():
    user = current_user.username
    user_id_queried = User.query.filter_by(username=user).first()
    return render_template("user_page.html",user=user_id_queried) 
