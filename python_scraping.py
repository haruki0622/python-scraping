import requests
from bs4 import BeautifulSoup

# 対象サイト
url = 'https://jp.indeed.com/jobs?q=プログラミング&l=大阪'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
jobCards = soup.select('.jobCard_mainContent')

data = []
for jobCard in jobCards:
  # 会社名
  companyName = jobCard.select_one('.companyName').text
  
  #会社住所
  companyLocation = jobCard.select_one('.companyLocation').text
  
  # 仕事内容
  jobTitle = jobCard.select_one('.jobTitle').text.replace('新着','')

  # 辞書の作成
  datum = {}
  datum['会社名'] = companyName
  datum['会社住所'] = companyLocation
  datum['仕事内容'] = jobTitle
  data.append(datum)
  
import pandas as pd
df = pd.DataFrame(data)
df.to_csv('company.csv',encoding='utf_8_sig',index=False)
