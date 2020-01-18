from urllib.request import urlopen
from bs4 import BeautifulSoup

# my_url = 'https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_2_na_na_na&as-pos=0&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=3272d8ec-ef28-4965-a6a6-4822b392f32e&as-searchtext=sa'
my_url = 'https://www.flipkart.com/search?q=honor+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_3_na_na_na&as-pos=0&as-type=RECENT&suggestionId=honor+mobiles%7CMobiles&requestId=72081454-39e3-4c4b-9e4b-9abc2a0aa25f&as-searchtext=honir'
url_response = urlopen(my_url)


url_data = url_response.read()
page_data = BeautifulSoup(url_data, "html.parser")
file_name = 'samsung_mobiles.csv'
headers = "Mobile , Price \n"

mobiles_data = page_data.findAll("div", {"class": "_1-2Iqu row"})
print(f"COUNT : {len(mobiles_data)}")
with open(file_name, "w", encoding="utf-8") as f:
    f.write(headers)
    for mobile in mobiles_data:
        mobile_name = mobile.div.div.text
        print(f"MOBILE NAME : {mobile_name}")
        mobile_prices_data = mobile.findAll("div", {
            "class": "_1vC4OE _2rQ-NK"})
        mobile_price = mobile_prices_data[0].text
        print(f"MOBILE PRICE : {mobile_prices_data[0].text}")
        f.write(mobile_name.replace(",", "-") + "," + mobile_price.replace(",", "-") + "," + "\n")
url_response.close()

