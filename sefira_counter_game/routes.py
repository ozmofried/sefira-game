from sefira_counter_game.user_login import LoginForm, SignupForm 
from sefira_counter_game import sefira_game2
from flask import Flask, render_template, request, redirect, flash, url_for,session,  g
from sefira_counter_game import app, db
from sefira_counter_game.dbmodels import User, Score  
from flask_login import login_user, current_user, logout_user, login_required
from time import sleep


player = sefira_game2.Game()
   


@app.route('/', methods=["POST", "GET"])
@login_required
def hello_world():
    
    #if player in session:
        #player = session["player"]

    
        guess = request.form.get("input_field")    
        
        if request.method == "POST":
            print(player.num)
            print(player.message)
            print(player.day)
            print(f"number guessed:{guess}" )
            player.guess_num(guess)
            
            return render_template("sefiracounter.html",score= player.score, day=player.day, n=player.message)
        
        else:
            print(player.num)
            print(player.message)
            print(player.day)
            return render_template("sefiracounter.html",score= player.score, day=player.day, n=player.message)
    #else:
        #redirect(url_for("login"))

@app.route('/timed_out', methods=["GET"])
@login_required
def timed_out():
    player.timed_out()
    #return render_template("timed_out.html")


@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    form = SignupForm()
 
    if form.validate_on_submit() and not form.validate_username(form.username) and not form.validate_email(form.email):
        flash("All Signed Up,\n Let's Play!!")
        new_user=User(username = form.username.data, email= form.email.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("hello_world"))
    else:    
        return render_template ('sign_up.html', title="Sign Up", form=form)

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
                #global player 
                player = current_user.username
                #print(type(player))
                #player = sefira_game2.Game()
                #print(type(player))
                #session["player"] = player
                
                flash(f"{user.username} Logged In")
                return redirect(url_for("hello_world"))
        else:
            flash("Login unsuccessful. Please try again.")
    return render_template ('login.html', title="Login", form=form)


@app.route('/rules')
def the_rules():
    return render_template("rules.html") 


@app.route('/logout')
def logout():
    game_score = Score(score= player.score, player= current_user) 
    db.session.add(game_score)
    db.session.commit()
    player.reset()
    logout_user()
    return redirect(url_for("login"))

@app.route('/user_page')
def user_page():
    user = current_user.username
    user_id_queried = User.query.filter_by(username=user).first()
    return render_template("user_page.html",user=user_id_queried) 
