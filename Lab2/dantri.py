from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

#1 Connect to the page
url = 'https://dantri.com.vn/' 
conn = urlopen(url)


#2.download the page content
raw_data = conn.read()
page = raw_data.decode('utf8')


# with open('dantri.html', 'wb') as f:
#     f.write(raw_data)



#3. find ROI region
soup = BeautifulSoup(page, 'html.parser')
ul = soup.find('ul', 'ul1 ulnew')
# print(ul.prettify())

#4.Extract data

li_list = ul.find_all('li')
news_list = []
for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a['href']

    new = {
       'title': title,
       'link': link,
   }
    news_list.append(new)
    

# print(a.string)
# print(a['href'])
#5. save data
pyexcel.save_as(records = news_list, dest_file_name="my_file.xls")
