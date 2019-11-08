from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def getWeather(url):
    #get page content via url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    #parsing
    weatherArray = soup.select("div.day.fields")
    result = []
    for day in weatherArray:
        dayresult = {}
        
        dayresult['tmax'] = int(day.find("div", {"class":"tmax"}).text.replace("°C",""))
        dayresult['tmin'] = int(day.find("div", {"class":"tmin"}).text.replace("°C",""))
        dayresult['freeText'] = day.find("div", {"class":"icon"}).find("img")['title']
        dayresult['neuschnee'] = day.find("div", {"class":"nschnee"}).text.replace("\n","").replace("cm","")
        
        if (dayresult['neuschnee'] == "-"):
            dayresult['neuschnee'] = 0
            
        if (dayresult['neuschnee'] == "<1"):
            dayresult['neuschnee'] = 1
            
        if (isinstance(dayresult['neuschnee'],str)):
            if (dayresult['neuschnee'].isnumeric()):
                dayresult['neuschnee'] = int(dayresult['neuschnee'])
        
        result.append(dayresult)
    return result

# > getWeather(url)
# [{'tmax': 3, 'tmin': 1, 'freeText': 'Schneeregen 0h Sonne', 'neuschnee': 3},
#  {'tmax': 1, 'tmin': 0, 'freeText': 'bedeckt 0h Sonne', 'neuschnee': 0},
#  {'tmax': 4, 'tmin': 2, 'freeText': 'wolkenlos 8h Sonne', 'neuschnee': 0},
#  {'tmax': 5, 'tmin': 0, 'freeText': 'wolkenlos 8h Sonne', 'neuschnee': 0},
#  {'tmax': 2, 'tmin': -1, 'freeText': 'wolkig 3h Sonne', 'neuschnee': 0},
#  {'tmax': 1, 'tmin': -2, 'freeText': 'wolkig 3h Sonne', 'neuschnee': 0},
#  {'tmax': 0, 'tmin': -3, 'freeText': 'stark bewölkt 1h Sonne', 'neuschnee': 1},
#  {'tmax': 0, 'tmin': -3, 'freeText': 'bedeckt 0h Sonne', 'neuschnee': 0},
#  {'tmax': 3, 'tmin': -3, 'freeText': 'wolkig 2h Sonne', 'neuschnee': 0}]
