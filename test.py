import requests
from bs4 import BeautifulSoup
import pandas as pd

# HTTP 요청 보내기
url = 'https://news.naver.com/section/101'
response = requests.get(url)
html = response.text

# HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 데이터 추출
articles = []
for a_tag in soup.find_all('a', class_='sa_text_title'):
    title = a_tag.find('strong', class_='sa_text_strong').get_text(strip=True)
    link = a_tag['href']
    articles.append({'title': title, 'link': link})

# 데이터 출력
for article in articles:
    print(article)

# 데이터 저장
df = pd.DataFrame(articles)
df.to_csv('naver_news_articles.csv', index=False)
