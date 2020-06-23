from flask import Flask, render_template, request

import sefira_game2
app = Flask(__name__)

new_game = sefira_game2.Game()

@app.route('/', methods=["POST", "GET"])
def hello_world():
    guess = request.form.get("input_field")    
    

    
    if request.method == "POST":
        print(new_game.num)
        print(new_game.message)
        print(new_game.day)
        new_game.guess_num(guess)
        return render_template("sefiracounter.html", day=new_game.day, n=new_game.message)
    else:
        
        print(new_game.num)
        print(new_game.message)
        print(new_game.day)
        return render_template("sefiracounter.html", day=new_game.day, n=new_game.message)










@app.route('/rules')
def the_rules():
    return '<body>These are the rules</body>'


if __name__ == '__main__':
    app.run(debug=True)
