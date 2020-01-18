from urllib.request import urlopen
from bs4 import BeautifulSoup

my_url = 'https://www.edureka.co/'
url_response = urlopen(my_url)
print(f"URL RESPONSE OBJECT : {url_response}")
url_data = url_response.read()
print(f"URL READED DATA : {url_data}")
# html parsing
page_data = BeautifulSoup(url_data, "html.parser")
# page_data = BeautifulSoup(url_data, "lxml")
print(f"PAGE DATA : {page_data}")
print(f"URL H1 READED DATA : {page_data.h1}")
# FIND ALL FUNCTION TO RETREIVE ALL THE REQUIRED TAGS
div_tags = page_data.findAll("li", {"class": "nav-item trending-cat-filter item ga-trending-cat-filter"})
print(f"FIND ALL FUNCTION : {div_tags}"
      f"\n TOTAL TAGS : {len(div_tags)}")
# Accesssing the necessary info from the data returned
print("Simple title : ", div_tags[0].a["title"])
li = []
for li_item in div_tags:
    li.append(li_item.a["title"])
print(f"RETREIVED TITLES : {li}")

# to grab the text from the webpage
li_text = []
for li_item in div_tags:
    li_text.append((li_item.a.text).strip())
print(f"TEXT RETREIVED : {li_text}")
url_response.close()

# ANOTHER WAY FOR EASY ACCESS (CAN BE TRIED)
# div_tags = page_data.find("li", {"class": "nav-item trending-cat-filter item ga-trending-cat-filter"})
# the below line    fetches both ul and ol
# div_tags = page_data.find({"ul","ol"}, {"class": "nav-item trending-cat-filter item ga-trending-cat-filter"})
# div = div_tags.find('li', style="background:red")
