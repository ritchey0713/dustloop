from bs4 import BeautifulSoup
from urllib.request import urlopen

#base url
url = 'https://www.dustloop.com/w/GGST'

# char list to iterate
chars = []

# bs4 open page to scrape includes (page, html, soup)
page = urlopen(url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

# get collection of html refering to char URL pages
char_container = soup.find("div", {"class": "add-hover-effect"})

# get all links to pages
charURLS = char_container.find_all('a')

#add each char to the chars List
for char in charURLS:
    chars.append(f"/{char['href'].split('/')[-1]}")

# FOR EACH element in the chars List, open page, and scrape data
page = urlopen(f'{url}{chars[0]}')

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

info_box = soup.find('div', {'class': 'home-card home-card--col2 home-card--row2'})

# need for JSON
name = info_box.find('div', {'class': 'home-card-title-large'}).text

info_box_table = info_box.find('table', {'class': 'infobox'})

charImg = f"https://www.dustloop.com{info_box_table.find('a').contents[0]['src']}"

# char data for jump frames etc
info_box_data = {}
for idx, data in enumerate(info_box_table.find_all('tr')):
    # print(f"hello: {data.text.lower().replace(' ', '_')} at idx: {idx}")
    if (idx == 0):
        None
    elif (idx % 2) == 0:
      info_box_data[info_box_table.find_all('tr')[idx -1].text.lower().replace(' ', '_')] = data.text
    else:
      info_box_data[data.text.lower().replace(' ', '_')] = ''

attack_containers = soup.find('div', {'id': 'mw-content-text'})

# print(attack_containers)
move_dict = {}

move_name_data = attack_containers.find_all('span', {'class':'mw-headline'})
move_name_list = move_name_data[2:]

# gets all normal moves notations
for move in move_name_list:
   if(" " not in move.text and len(move.text) < 4):
    move_dict[move.text] = ''




