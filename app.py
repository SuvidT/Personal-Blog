"""
This is the main application file for the project.
It initializes the app and the routes
"""

# ------------------------
# IMPORTS
# ------------------------
from flask import Flask, render_template, abort, session, redirect, url_for, request, flash
from markupsafe import escape

from articles import get_article, get_articles
from users import check_login, make_account

# ------------------------
# CONSTANTS
# ------------------------
app = Flask(__name__)
app.secret_key = "FakeKey"

# ------------------------
# ERRORS
# ------------------------
@app.errorhandler(400)
def bad_request(e):
    return render_template("error.html", e=e), 400


@app.errorhandler(403)
def forbidden(e):
    return render_template("error.html", e=e), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", e=e), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template("error.html", e=e), 405


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error.html", e=e), 500

# ------------------------
# ROUTES
# ------------------------
@app.route('/')
@app.route('/articles/')
def articles():
    articles = get_articles()

    user = session.get('user')
    return render_template("articles.html", articles=articles, user=user)

@app.route('/articles/<int:num>')
def article(num):
    article = get_article(num)

    if article is None:
        abort(404)

    user = session.get('user')
    return render_template("article.html", article=article, user=user)

@app.route('/signup')
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')

        if password != confirm:
            flash("Passwords do not match")
            return redirect(url_for('signup'))

        success, message = make_account(username, password, email)
        if success:
            flash("Account created! Please log in.")
            return redirect(url_for('login'))
        else:
            flash(message)
            return redirect(url_for('signup'))

    return render_template("signup.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if check_login(username, password):
            session['user'] = username
            return redirect(url_for('articles'))
        
        flash("Invalid login")

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('articles'))

# ------------------------
# RUNNING
# ------------------------
if __name__ == '__main__':
    app.run(debug=True)
