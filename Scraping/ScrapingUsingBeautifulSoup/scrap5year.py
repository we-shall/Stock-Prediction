import requests
from bs4 import BeautifulSoup
import pandas as pd
import arrow
import urllib2 as urb
#code is in python2
#this code is for extracting 5 years news from business standard website
#you can do this for websites like moneycontrol and IIFL etc.
for year in range (2015,2018):
    for month in range (1,12):
        for day in range (1,31):

            if ( month < 10):
                monthstr = '0' + str(month)
            if ( day < 10):
                daystr = '0' + str(day)
            yearstr = str (year)
            try:
                r = requests.get('http://www.business-standard.com/todays-paper/?print_dd='+daystr+'&print_mm='+monthstr+'&print_yy='+yearstr);
            except:
                print("link invalid")
                pass
            print ('link accessed')
            soup = BeautifulSoup(r.content,"html.parser")
            for data in soup.select("ul li h2 a"):
                        html = urb.urlopen("http://www.business-standard.com/"+data.get("href"))
                        soup1 = BeautifulSoup(html, "html.parser")
                        for  item in soup1.select(".p-content p"):
                            print (item.get_text() + "")
                        print ("\n\n\n")

