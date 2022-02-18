from flask import Flask, render_template, request
from predict import link, classify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/prediction", methods=["GET", "POST"])
def pred():
    try:
        text = link(request.form["url"])
        values = classify(text)
        pred, prob = values['prediction'], int(values['probability'] * 1000)/10
        prob = round(prob, 3)
    except:
        prob, pred = 200, None
        text = 'invaild URL'
    return render_template("pred.html", pred=pred, prob=prob, text=text)


if __name__ == "__main__":
    app.run(debug=True)
