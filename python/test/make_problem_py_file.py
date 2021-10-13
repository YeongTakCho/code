import os
import os.path, time
import requests
from bs4 import BeautifulSoup


def blog_crawling():
    url = input('input url: ')
    path = 'C:\\Users\\s_andycho1120\\code\\python\\백준\\'

    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    spans = [span for span in soup.select('span')]

    problem_num = str(spans[3])[26:-12]
    problem_name= str(spans[4])[25:-7]

    file_name= path + problem_num +'- ' + problem_name + '.py'

    if os.path.isfile(file_name):
        print('File is exist ' + file_name+'\n')
        
        print("Modified : ")
        print(time.ctime(os.path.getmtime(file_name)))
        print("Created : ")
        print(time.ctime(os.path.getctime(file_name)))
        print("Accessed : ")
        print(time.ctime(os.path.getatime(file_name)))
    else:
        open(file_name,'w')
        print('File is created')

    os.system('pause')
    
blog_crawling()