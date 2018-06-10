import requests
from bs4 import BeautifulSoup

# this code will scrap data of the date entered by the user..


print ("enter the date in DD/MM/YYYY")
date = raw_input()
day = date[:2]
month = date[3:-5]
year = date[-4:]
#you can make the link dynamic by iterating it into for loop
r = requests.get('http://www.business-standard.com/todays-paper/?print_dd='+day+'&print_mm='+month+'&print_yy='+year);
soup = BeautifulSoup(r.content,"html.parser")

#print (soup.prettify())
topBdata = soup.find_all ("div",{"class":"topB"})


#this data can be stored in csv format
for dataCluster in topBdata:
    for data in dataCluster.find_all("ul",{"class":"aticle-txt"}):
        print (data.text)


