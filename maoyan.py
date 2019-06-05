import requests
import re
import copy
from bs4 import BeautifulSoup
from prettytable import PrettyTable
def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

#def main():
list_file = open("movielist",'w')
table=PrettyTable(["排行","名称","主演","上映时间","评分"])
for num in range(0,5):
	url = 'http://maoyan.com/board/4'+'?offset='+str(num*10)
	html = get_one_page(url)
#print(html)
	soup =BeautifulSoup(html,'lxml')
	items=soup.find_all('dd')
	i=0
	for item in items:
		html_page=soup.find_all('dd')[i]
		index=html_page.find('i',class_='board-index').get_text()
		name=html_page.find('p',class_='name').a['title']
		star=html_page.find('p',class_='star').get_text().strip().strip('主演：')
		releasetime=html_page.find('p',class_='releasetime').get_text().strip().strip('上映时间：')
		score=html_page.find('i',class_='integer').get_text()		+html_page.find('i',class_='fraction').get_text()
		list_=str(index)+str(name)+str(star)+str(releasetime)+str(score)+'\n'
		table.add_row([index,name,star,releasetime,score])
		#print(index,name,star,releasetime,score)
		i=i+1	
print(table)
list_file.write(str(table))


