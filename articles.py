# ------------------------
# IMPORTS
# ------------------------
from os import path
from datetime import datetime
import json
import markdown

# ------------------------
# CONSTANTS
# ------------------------
json_file = 'metadata/articles.json'
md_files_path = 'articles/'

# ------------------------
# FUNCTIONS
# ------------------------
def get_article(article_title):
    '''
    Here's what this function does:
    1) Declare 
    '''
    md_file = md_files_path + f'{article_title}.md'
    article = {"title": f"{article_title}", "date": "April 1, 2025", "author": "Dev", "content": None}

    if not path.exists(md_file):
        article["content"] = "<p>This article does not exist</p>"
        return article
    
    with open(json_file, "r") as file:
        data = json.load(file)
    
    if data[f"{article_title}"]["archived"] == True:
        article["content"] = "<p>This article has been archived</p>"

    data = data[f"{article_title}"]

    article["date"] = datetime(data["date"][0], data["date"][1], data["date"][2]).strftime("%B %d, %Y")
    article["author"] = data["author"]

    with open(md_file, )

def get_articles():
    pass