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
def get_article(num):
    """
    Retrieves an article's metadata and content based on its index in the JSON file.

    Args:
        num (int): The index of the article in the JSON file.

    Returns:
        dict: A dictionary containing the article's details:
            - title (str): The title of the article.
            - author (str): The author of the article.
            - date (list): The publication date as [Year, Month, Day].
            - num (int): The unique identifier for the article.
            - archived (bool): Whether the article is archived.
            - content (str): The content of the article in Markdown format.

        None: If the index is invalid, the article is archived, or the article does not exist.
    """

    # gets metadata about articles from the json file
    with open(json_file, "r") as file:
        data = json.load(file)

    # checks if the num is valid
    if len(data) >= num or data[num] == 0:
        return None
    
    # stores the metadata we wanted from the article in article
    article = data[num]

    # checks if the article is archived
    if article["archived"] == True:
        return None

    # gets the content of the markdown file with the title of the article  
    md_file = md_files_path + f"{article["title"]}.md"
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    # puts the content into the article dict
    article["content"] = content

    # returns the article metadata and content
    return article


def get_articles():
    """
    Retreives the metadata from articles.json and returns a list of articles,
    in the reverse order of when the were made/eddited.

    Args: --

    Returns:
        list: a list containig dicts:
            dict: a dict for each article
    """

    # opens the json file and stores the data in the variable data
    with open(json_file, "r") as file:
        data = json.load(file)

    # sandardizes the dates as a number so that we can compare
    def std_date(date):
        return date[0] + ((date[1] - 1)/12) + date[2]/3100
    
    # this is the function to sort the array
    def quicksort(arr):
        # base case
        if len(arr) <= 1:
            return arr
        
        # choosing the middle as the pivot 
        pivot = arr[len(arr) // 2]

        # partition the arry into two subarrays
        less = [article for article in arr if std_date(article["date"]) > std_date(pivot["date"])]
        greater = [article for article in arr if std_date(article["date"]) <= std_date(pivot["date"]) and article != pivot]

        # recursive call
        return quicksort(less) + [pivot] + quicksort(greater)
    
    return quicksort(data)

# ------------------------
# TESTING
# ------------------------
