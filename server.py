from flask import Flask, render_template

app = Flask(__name__)
# By default, Flask look for files on the folder templates
# There is host the index.html

@app.route("/")
def hello_world():
    return render_template("html5up-astral/index.html")


if __name__ == "__main__":
    app.run(debug=True)
