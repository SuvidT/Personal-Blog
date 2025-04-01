"""
This is the main application file for the project.
It initializes the app and the routes
"""

# ------------------------
# IMPORTS
# ------------------------
from flask import Flask, render_template

# ------------------------
# CONSTANTS
# ------------------------
app = Flask(__name__)

# ------------------------
# ROUTES
# ------------------------
@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors by returning a custom error message.

    Args:
        e (HTTPException): The exception object containing details about the error.

    Returns:
        tuple: A tuple containing the HTML response and the HTTP status code (404).
    """
    return render_template("error.html", e=e), 404

# ------------------------
# RUNNING
# ------------------------
if __name__ == '__main__':
    app.run(debug=True)
