import os
from bs4 import BeautifulSoup
from bs4.element import Tag
import cfscrape


def setlistofphoto():


    scraper = cfscrape.create_scraper()
    r = scraper.get("https://bbaggome.com/yajjal_board?page=1")
    r.status_code  # 200

    bs= BeautifulSoup(r.content.decode('utf-8'),'html.parser')
    
    class_name= '.info_right'
    for data in bs.select(class_name):
        print(data)

    
setlistofphoto()


