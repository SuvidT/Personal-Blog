"""
This is the main application file for the project.
It initializes the app and the routes
"""

# ------------------------
# IMPORTS
# ------------------------
from flask import Flask, render_template, abort
from markupsafe import escape

from articles import get_article, get_articles
import users

# ------------------------
# CONSTANTS
# ------------------------
app = Flask(__name__)

# ------------------------
# ERRORS
# ------------------------
@app.errorhandler(400)
def bad_request(e):
    """
    Handles 400 Bad Request errors.

    Args:
        e (HTTPException): The exception object containing details about the error.

    Returns:
        tuple: A tuple containing the rendered error template and the HTTP status code (400).
    """
    return render_template("error.html", e=e), 400


@app.errorhandler(403)
def forbidden(e):
    """
    Handles 403 Forbidden errors.

    Args:
        e (HTTPException): The exception object containing details about the error.

    Returns:
        tuple: A tuple containing the rendered error template and the HTTP status code (403).
    """
    return render_template("error.html", e=e), 403


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 Not Found errors.

    Args:
        e (HTTPException): The exception object containing details about the error.

    Returns:
        tuple: A tuple containing the rendered error template and the HTTP status code (404).
    
    """
    return render_template("error.html", e=e), 404


@app.errorhandler(405)
def method_not_allowed(e):
    """
    Handles 405 Method Not Allowed errors.

    Args:
        e (HTTPException): The exception object containing details about the error.

    Returns:
        tuple: A tuple containing the rendered error template and the HTTP status code (405).
    """
    return render_template("error.html", e=e), 405


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handles 500 Internal Server Error errors.

    Args:
        e (HTTPException): The exception object containing details about the error.

    Returns:
        tuple: A tuple containing the rendered error template and the HTTP status code (500).
    """
    return render_template("error.html", e=e), 500

# ------------------------
# ROUTES
# ------------------------
@app.route('/')
@app.route('/articles/')
def articles():
    articles = get_articles()

    return render_template("articles.html", articles=articles)

@app.route('/articles/<int:num>')
def article(num):
    article = get_article(num)

    if article is None:
        abort(404)

    return render_template("article.html", article=article)

# ------------------------
# RUNNING
# ------------------------
if __name__ == '__main__':
    app.run(debug=True)
