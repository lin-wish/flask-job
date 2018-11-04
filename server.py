from flask import Flask, render_template, request
from search import *
from flask_login import LoginManager
from filters import compute_ago

app = Flask(__name__)
app.jinja_env.filters['compute_ago'] = compute_ago
app.secret_key = "test"

login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def home():
    return render_template('index.html')



@app.route("/search")
def search():
    data = request.args
    keyword = data["q"]
    jobs = []
    results = search_reddit(query = keyword)
    jobs = [r for r in results]
    

    return render_template("results.html", post_list = jobs)


@app.route("/email")
def email_form():
    return app.render_template("email.html")

if __name__ == '__main__':
    app.run(debug=True)
