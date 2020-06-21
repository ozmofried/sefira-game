from flask import Flask, render_template, request

import sefira_game2
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def hello_world():
    guess = request.form.get("input_field")
    if sefira_game2.today["number"] is None:
        sefira_game2.number_picker()

    print(sefira_game2.today.values())

    if request.method == "POST":
        sefira_game2.guess_num(guess)
        return render_template("sefiracounter.html", day=sefira_game2.today["day"], n=sefira_game2.today["message"])
    else:

        return render_template("sefiracounter.html", day=sefira_game2.today["day"], n=sefira_game2.today["message"])










@app.route('/rules')
def the_rules():
    return '<body>These are the rules</body>'


if __name__ == '__main__':
    app.run(debug=True)
