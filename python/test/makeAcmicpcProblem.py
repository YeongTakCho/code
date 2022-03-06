import os
import os.path, time
import requests
from bs4 import BeautifulSoup


def makeAcmicpcProblem():
    path = 'C:\\Users\\s_andycho1120\\code\\python\\백준\\'



    print('!!! WARNING : IT IS ONLY FOR ACMICPC.NET PROBLEM URL !!!')

    url = input('input url: ')
    
    if url[:32] != 'https://www.acmicpc.net/problem/':
        
        print('\n THAT IS WRONG URL, PLEASE CHECK YOUR URL\n')
        return


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = str(soup.select('title'))
    print(title)
    problem_num = url[32:]
    problem_name= title[len(problem_num)+11:-9]
    
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

    

    
makeAcmicpcProblem()
os.system('pause')
