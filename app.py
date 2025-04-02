"""
This is the main application file for the project.
It initializes the app and the routes
"""

# ------------------------
# IMPORTS
# ------------------------
from flask import Flask, render_template
from markupsafe import escape
from articles import get_article, get_articles

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
def home():
    return "<h1> TODO: Home Page </h1>"

@app.route('/articles/<articleName>')
def article(articleName):
    safe_article_name = escape(articleName)
    formatted_article_name = safe_article_name.replace("_", " ")

    article = get_article(formatted_article_name)

    return render_template("article.html", article=article)

# ------------------------
# RUNNING
# ------------------------
if __name__ == '__main__':
    app.run(debug=True)
