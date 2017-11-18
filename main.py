from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def myFunc(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    weatherArray = soup.find_all("div", {"day clickable selectable fields"})
    i = 0
    for day in weatherArray:
        myDate = datetime.now().date() + timedelta(days=i)

        tmax = day.find("div", {"class":"tmax"}).text
        tmin = day.find("div", {"class":"tmin"}).text
        freeText = day.find("div", {"class":"icon"}).find("img")['title']

        try:
            snow = day.find("div", {"class":"group nschnee important"}).text.replace("\n","").replace("\t","").replace(" ","")
        except:
            snow = day.find("div", {"class":"group nschnee "}).text.replace("\n","").replace("\t","").replace(" ","")

        print(str(myDate) + " weekday: " + str(myDate.weekday()) + " - " + "Neuschnee: " + snow + ", " + str(freeText) + " bei " + tmin + " bis " + tmax)
        i += 1

kitzUrl = "http://www.bergfex.at/kitzsteinhorn-kaprun/wetter/berg/"

urls= [
"http://www.bergfex.at/kitzsteinhorn-kaprun/wetter/berg/",
"http://www.bergfex.at/obertauern/wetter/berg/",
"http://www.bergfex.at/zell-am-ziller/wetter/berg/",
"http://www.bergfex.at/zauchensee/wetter/berg/",
"http://www.bergfex.at/flachau-wagrain-alpendorf/wetter/berg/"
]

print(" ")
for url in urls:
    print(url.split('/')[3])
    myFunc(url)
    print(" ")
