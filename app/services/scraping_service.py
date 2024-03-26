import logging
import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    '''
    Function does the following:
    1. Takes URL as input and fetches the HTML content of the webpage
    2. Parse the HTML content using BeautifulSoup
    3. Extract the textual content and returns it as a string
    '''

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text(separator="\n")

    return text
