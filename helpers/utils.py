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

#Function to obtain the information of a genera from its url
def get_genera_info(url: str) -> dict:
    bs = load_html(BASE_URL + url)
    div_container = bs.find(
        "div", 
        class_="sidebar-content-sect__content__content-block"
        )
    
    #Get the name of the genera
    name = div_container.find("h1")

    #Get the discovery of the genera
    discovery = name.find_next_sibling("p")

    #Get the description of the genera
    description = discovery.find_next_sibling("p")

    #Get number of species
    species = description.find_next_sibling("p")

    #Get the distribution of the genera
    distribution = species.find_next_sibling("p")

    try:
        return {
            "name": name.text,
            "discovery": discovery.text,
            "description": description.text,
            "species": species.text,
            "distribution": distribution.text
        }  
    except AttributeError:
        return {
            "name": name.text,
            "discovery": None,
            "description": discovery.text,
            "species": description.text,
            "distribution": species.text,
        }
