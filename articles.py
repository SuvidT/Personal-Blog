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
    """
    Retrieves an article's metadata and content, converting the Markdown content to HTML.

    Args:
        article_title (str): The title of the article (used to locate the Markdown file and metadata).

    Returns:
        dict: A dictionary containing the article's details:
            - title (str): The title of the article.
            - date (str): The publication date in the format "Month Day, Year".
            - author (str): The author of the article.
            - content (str): The HTML content of the article. If the article is archived or does not exist,
              a corresponding message is returned instead.
    """

    md_file = md_files_path + f'{article_title}.md'
    article = {
        "title": f"{article_title}", 
        "date": datetime.now().strftime("%B %d, %Y"), 
        "author": "Dev", 
        "content": None
        }

    if not path.exists(md_file):
        article["content"] = "<p>This article does not exist</p>"
        return article
    
    with open(json_file, "r") as file:
        data = json.load(file)
    
    if data[f"{article_title}"]["archived"] == True:
        article["content"] = "<p>This article has been archived</p>"
        return article

    data = data[f"{article_title}"]

    article["date"] = datetime(data["date"][0], data["date"][1], data["date"][2]).strftime("%B %d, %Y")
    article["author"] = data["author"]

    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    article["content"] = markdown.markdown(content)

    return article

def get_articles():
    with open(json_file, "r") as file:
        data = json.load(file)
    
    

# ------------------------
# TESTING
# ------------------------
