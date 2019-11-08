from bs4 import BeautifulSoup
import requests

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
        dayresult['probability'] = day.find("div", {"class": "rrp"}).text.replace("\n","").replace("%","")
        dayresult['sun'] = day.find("div", {"class": "sonne"}).text.replace("\n","").replace("h","")
        
        if (dayresult['neuschnee'] == "-"):
            dayresult['neuschnee'] = 0
            
        if (dayresult['neuschnee'] == "<1"):
            dayresult['neuschnee'] = 1
            
        if (isinstance(dayresult['neuschnee'],str)):
            if (dayresult['neuschnee'].isnumeric()):
                dayresult['neuschnee'] = int(dayresult['neuschnee'])
        
        if (dayresult['probability'].isnumeric()):
            dayresult['probability'] = int(dayresult['probability'])
        
        if (dayresult['sun'].isnumeric()):
            dayresult['sun'] = int(dayresult['sun'])
        
        if (dayresult['sun'] == "-"):
            dayresult['sun'] = 0
        
        result.append(dayresult)
    return result
