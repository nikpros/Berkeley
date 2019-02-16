import requests
import sys, os
from bs4 import BeautifulSoup

#-- На этой стадии мы определямся с количеством обрабатываемых html-страниц
url_const = "https://escholarship.org"
url = "https://escholarship.org/search?campuses=ucb&departments=iber_resin&departments=citris&departments=crest&departments=cedr&disciplines=Engineering&disciplines=Physical+Sciences+and+Mathematics&type_of_work=article"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
nav = soup.find('nav', class_='c-pagination--next').find('li', class_='c-pagination__next')
count = nav.previous_sibling.get_text()
print(count)
url_1 = 'https://escholarship.org/search?campuses=ucb&departments=iber_resin&departments=citris&departments=crest&departments=cedr&disciplines=Engineering&disciplines=Physical+Sciences+and+Mathematics&start='
url_2 = '&type_of_work=article'
i = 10 #--переменная для контакенации нового urlа
iter = 1 #--переменная для названия нового документа
#---------------------------------------#
#--Отсюда начинается цикл обхода всех ссылок с дейтсвующими download-ами на каждой html-странице
while i < 30: #(int(count)+1)*10: Боевой цикл на скачивание 406 PDF-документа 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    heading = soup.find_all('heading')
    for head in heading:
        href = head.find('a').get('href')
        r = requests.get(url_const + href)
        soup = BeautifulSoup(r.text, 'html.parser')
        href_dow = soup.find('div', class_='o-download').find('a').get('href')
        print(href_dow)
    #Download PDF-file
        pdf = requests.get(href_dow)
        
        #--Определение текущей директории
        pathname = os.path.dirname(sys.argv[0])        
        newpath = os.path.abspath(pathname) + '/pdf'
        #--Создание в текущей директории каталога pdf
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        f = open("pdf/{}.pdf".format(iter), "wb")
        f.write(pdf.content)
        f.close()
        iter += 1
        print(iter)
        url = url_1 + str(i) + url_2
    i += 10





#section = soup.find('section', class_='o-columnbox1').find_all('section', class_='c-scholworks')
#for sec in section:
#    href = section.find('heading').find('a').get('href')
#print(heading)


