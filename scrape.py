# REMEMBER: DON'T DO ILLEGAL SCRAPING
# REMEMBER: CHECK THE <url>/robots.txt FILE TO SEE WHAT INFO YOU ARE ALLOWED TO SCRAPE
# REMEMBER: WEB SCRAPING IS SPECIFIC TO THE CONTENT OF THE WEBSITE, SO CHECK THE WEB-PAGE CONTENT WHILE WRITING
# YOUR SCRAPER
# REMEMBER: MANY WEBSITES PROVIDE DATA ACCESS THROUGH API. WEB SCRAPING MAY NOT BE NEEDED IN SUCH WEBSITES.
# NOTE: 'scrapy' IS A FRAMEWORD ENTIRELY DEDICATED TO SCRAPING LARGE AMOUNTS OF DATA FROM THE WEB 

from re import sub
import requests  # To send HTTP requests and get back HTML content from the web
# To Use the HTML content for scraping useful information
from bs4 import BeautifulSoup
import pprint  # built-in python module for printing data in a visually pleasing format

# Get HTML content from the News page of Hacker News Website, similar to a Browser, without rendering the HTML
res = requests.get('https://news.ycombinator.com/news')
# print(res.text) # Print the entire HTML content as text
# Parse the HTML content into a python data structure that can be manupulated
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.body.contents)  # list of the tags within the body of the HTML page
print()
print()
print("All divs in HTML : ")
# Prints all the <div> tags in the soup object as a list
print(soup.find_all('div'))
print()
print("soup.find('a') : ")
print(soup.find('a'))  # Prints the first <a> tag from the soup object
print()
# print the first tag with the specified id
print("soup.find(id='score_33221780') : ", soup.find(id='score_33221780'))

print()
print()

# Using CSS selectors to choose parts of the 'soup' object
print("soup.select('a') : ")
# select all the a tags using CSS selector from the soup object
print(soup.select('a'))
print()
print()
print("soup.select('.score') : ")
# Select all the tags from the soup object with class name 'score'
print(soup.select('.score'))
print()
print()
print("soup.select('#score_33221780') : ")
# Select all the tags from the soup object with id 'score_33221780'
print(soup.select('#score_33221780'))

print()
print()

# Select all the <spans> with class 'titleline' and
links = soup.select('.titleline > a')
# get the <a> tags within them as a list
# Grab all the elements that have the class 'subtext' from the BeautifulSoup object
subtext = soup.select('.subtext')
print(subtext[0])
# REMEMBER: The first link and the first vote correspond to each other. Hence, 'links' and 'votes' are in the same
# order
print()
# get attributes from a particular tag element in the list of tag elements
print("subtext[0].get('class') : ", subtext[0].get('class'))
# selected tags from the soup object


# Function to sort list of dictionaries by the value of 'votes' key
def sort_stories_by_vote(hnlist):
    # Sort using the 'votes' key in descending order
    return sorted(hnlist, key=lambda x: x['votes'], reverse=True)

# Function to print the links and votes in a pretty format


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()  # get the text inside the tag
        # grab the href attribute from the tag. If the href tag is not present, href will be set to None
        href = item.get('href', None)
        # Select the child element with class-name 'score' from each <span> as a list
        vote = subtext[idx].select('.score')
        if len(vote):  # If the child element containing the votes exists within the span with class 'score'
            # extract the number of votes as an int from the single-element list
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:  # keep only the links that have votes > 99
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_vote(hn)


# pprint.pprint(create_custom_hn(links, subtext)) # print the list of dictionaries in a pretty format
print()
print()
print()
# Repeat same thing for Page 2 of Hacker News Website
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')
mega_links = links + links2  # combine two lists of tag elements
mega_subtext = subtext + subtext2  # combine both lists of tag elements
# print the list of dictionaries in a pretty format
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
