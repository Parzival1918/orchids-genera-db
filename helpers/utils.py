import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.aos.org"
LIST_URL = "https://www.aos.org/orchids/orchids-a-to-z.aspx"

SAVE_LOC = "db"

#Function to load the html of a link into a BeautifulSoup object
def load_html(url) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

#Function to get all the links in href from a BeautifulSoup object
def get_links(soup: BeautifulSoup) -> list[str]:
    links = []
    for link in soup.find_all('a', href = True):
        links.append(link['href'])
    return links

#Function from a list of links get those that contain a string
def match_links(links: list[str], match: str) -> list[str]:
    return [link for link in links if match in link]