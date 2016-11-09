import requests
from bs4 import BeautifulSoup
import subprocess
import time

def main():
    url = "http://www.bbc.co.uk/news/popular/read"  # URL of the page where 10 most popular news stories are available.
    response = requests.get(url)  # send a GET request using the specified URL and save the resulting response.

    soup = BeautifulSoup(response.content, "html.parser")  # Create a BeautifulSoup object using the requested HTML doc.

    most_popular = soup.find_all("a", {"class": "most-popular-page-list-item__link"})  # Get the <a> tags with stories.

    stories = {}  # Create a dict to store the title and links for popular news stories. Order won't be maintained.

    for anchor in most_popular:
        link = anchor.get("href")
        title = anchor.contents[3].text
        stories[title] = link  # Save the title and link of the story and key, value pair within the dict.

    for story in stories:
        url = stories[story]  # Get the URL for the current story.
        response = requests.get("http://www.bbc.co.uk{}".format(url))  # Make a GET request for the above URL.

        soup = BeautifulSoup(response.content, "html.parser")  # Create a BeautifulSoup object of the current story.
        introduction = soup.find("p", {"class": "story-body__introduction"}).text  # Find the intro for the story.
        print("Title: {} \nURL: http://www.bbc.co.uk{}\nIntroduction: {}\n".format(story, stories[story], introduction))
	
	top_news_raw = 'Here is one thing happening around the world. %s. Here is the summary. %s' % (story, introduction)
	top_news = top_news_raw.replace('"',' ')
	print top_news
	# Checks if the room is empty or not through darknet
	with open('../../Pictures/darknet/meeting.csv', 'r+') as f:
            text = f.read()
	    if 'Meeting is off' in text:		
        	command = 'gtts-cli.py "%s" -l "en" -o news.mp3 && play news.mp3' % top_news
        	subprocess.call(command, shell=True)
		f.truncate()
	    else:
		pass
		f.truncate()
        time.sleep(600)

if __name__ == "__main__":
    while True:
