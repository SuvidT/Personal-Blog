# ------------------------
# IMPORTS
# ------------------------
from os import path, remove
from datetime import datetime
import json
from markdown import markdown

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
    # checks if the markdown file exists
    md_file = md_files_path + f"{article["title"]}.md"
    if not path.exists(md_file):
        return None

    # gets metadata about articles from the json file
    with open(json_file, "r") as file:
        data = json.load(file)

    # checks if the num is valid
    if len(data) <= num or num < 0 or data[num] == 0:
        return None
    
    # stores the metadata we wanted from the article in article
    article = data[num]

    # checks if the article is archived
    if article["archived"] == True:
        return None

    # gets the content of the markdown file with the title of the article  
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    # puts the content into the article dict
    article["content"] = markdown(content)

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

        if pivot["archived"] or pivot == 0:
            arr.remove(pivot)
            return quicksort(arr)

        # partition the arry into two subarrays
        less = [article for article in arr if article != 0 and std_date(article["date"]) > std_date(pivot["date"]) and article["archived"] == False]
        greater = [article for article in arr if article != 0 and std_date(article["date"]) <= std_date(pivot["date"]) and article != pivot and article["archived"] == False]

        # recursive call
        return quicksort(less) + [pivot] + quicksort(greater)
    
    return quicksort(data)


def add_article(article):
    '''
    article
    - title
    - author
    - date
    - content
    '''

    # Loads all the data from the json file as data
    with open(json_file, "r") as file:
        data = json.load(file)

    if article["date"] == None:
        article["date"] = datetime.now().strftime("%Y-%m-%d")

    # setting up variables
    # metadata is what will be put in the articles.json
    metadata = {
        "title": article["title"],
        "author": article["author"],
        "date": article["date"],
        "num": len(data),
        "archived": False
        }
    # this is the file path of the newly created article
    md_file = md_files_path + f"{article["title"]}.md"
    # this is the content that will be put in the markdown file
    content = article["content"]

    # this is the part where we add the article metadata into the data
    # this will replace the first 0 in the list, or add at the end
    replaced = False
    for index, article in enumerate(data):
        if article == 0:
            metadata["num"] = index
            data[index] = metadata
            replaced = True
    if not replaced:
        data.append(metadata)

    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)

    with open(md_file, "w", encoding="utf-8") as file:
        file.write(content)
    
def archive_article(num):
    # getting the data from json as data
    with open(json_file, "r") as file:
        data = json.load(file)

    # archiving the article at num
    data[num]["archived"] = True

    # inserting the data back in
    with open(json.file, "w") as file:
        json.dump(data, file, indent=4)

def delete_article(num):
    with open(json_file, "r") as file:
        data = json.load(file)

    data[num] = 0

    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)

# ------------------------
# TESTING
# ------------------------


delete_article(3)
