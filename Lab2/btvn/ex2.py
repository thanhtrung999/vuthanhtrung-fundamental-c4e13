from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

#1 Connect to the page
url = 'https://www.apple.com/itunes/charts/songs/' 
conn = urlopen(url)
#2.download the page content
raw_data = conn.read()
page = raw_data.decode('utf8')
#3. find ROI region
soup = BeautifulSoup(page, 'html.parser')
ul = soup.find('ul', '')
#4.Extract data

li_list = ul.find_all('li')
news_list = []
for li in li_list:
    a = li.a
    h3 = li.h3
    h4 = li.h4
    title = a.string
    singer = h4.string
    link = url + a['href']

    new = {
       'title': title,
       'singer': singer,
       'link': link,
   }
    news_list.append(new)
#5. save data
pyexcel.save_as(records = news_list, dest_file_name="ex2_itunes.xls")