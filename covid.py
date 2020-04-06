from bs4 import BeautifulSoup
import requests
r=requests.get("https://www.worldometers.info/coronavirus/")
soup=BeautifulSoup(r.text,"lxml")
data=soup.find_all("table",{"id":"main_table_countries_yesterday"},{"class":"table table-bordered table-hover main_table_countries dataTable no-footer"})
data=data[0]
for trs in data.find_all("tr"):
    for td in trs.find_all("td"):
        print(td.string,end="    ")
    print()