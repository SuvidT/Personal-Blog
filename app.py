"""
This is the main application file for the project.
It initializes the app and the routes
"""

# ------------------------
# IMPORTS
# ------------------------
from flask import Flask

# ------------------------
# CONSTANTS
# ------------------------
app = Flask(__name__)

# ------------------------
# ROUTES
# ------------------------
@app.errorhandler(404)
def page_not_found(e):
    # TODO: implement 404 html page
    return f"<h1>{e.code} - {e.name}</h1><p>{e.description}</p>", 404

# ------------------------
# RUNNING
# ------------------------
if __name__ == '__main__':
    app.run(debug=True)
