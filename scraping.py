from bs4 import BeautifulSoup
import requests
import pandas as pd
rows_count = 0
while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data,'html.parser')
    rows = soup.find_all('tr',{'class':['odd','even']})
    rows_count = 0
    for row in rows:
        columns = row.find_all('td')
        link = row.find('a').get('href')
        link = "https://www.programmableweb.com/category/tools/api"+str(link)
        rows_count+=1
        c[rows_count] = [columns[0].text,columns[1].text,columns[2].text,link]
    next_url = soup.find('li',{'class':'pager-next'}).find('a')
    if next_url.get('href'):
        url = "https://www.programmableweb.com/category/tools/api"+next_url.get('href')
    else:
        break
print(rows_count)
df = pd.DataFrame.from_dict(c,orient='index',columns=['name','dexcription','category','link'])
df.to_csv('salman.csv')    
