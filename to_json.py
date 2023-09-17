from helpers import utils
import json
import os

#Create folder to store the json files
path = utils.SAVE_LOC + "/json"
if not os.path.exists(path):
    os.makedirs(path)

#Function to save the json file
def save_json(data: dict, name: str):
    with open(path + "/" + name + ".json", "w") as file:
        json.dump(data, file, indent=4)

#Load source page
print("Loading page to bs4... ", end="")
bs = utils.load_html(utils.LIST_URL)
print("Done")

#Get all links from page
print("Getting links from page... ", end="")
links = utils.get_links(bs)
print("Done")

#Filter links
print("filtering links... ", end="")
filtered = utils.match_links(links, '/orchids/orchids-a-to-z/')
print("Done", end="\n\n")

#Iterate over every link found to obtain the information of every genera
for genera_link in filtered[16:]:
    print(f"Obtaining data from: {genera_link}... ", end="")

    #From genera_link obtain the letter we are searching
    split_txt = genera_link.split("/")
    search_letter = split_txt[-1].removesuffix(".aspx")

    #Get all links from page
    bs = utils.load_html(utils.BASE_URL + genera_link)
    links = utils.get_links(bs)

    #Filter links
    filtered = utils.match_links(links,'/orchids/orchids-a-to-z/'+search_letter+"/")

    print("Done")

    data_dict = []
    for genera_filtered in filtered:
        print(f" - Obtaining data from: {genera_filtered}... ", end="")

        info = utils.get_genera_info(genera_filtered)
        data_dict.append(info)

        print("Done")

    print("Saving data to json file... ", end="")
    save_json(data_dict, search_letter)
    print("Done", end="\n\n")

        