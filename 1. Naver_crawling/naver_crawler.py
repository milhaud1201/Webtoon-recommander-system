# 필요한 라이브러리 호출
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
from tqdm import tqdm
import time
import re
import requests
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# 연재중인 네이버 웹툰 정보 크롤링 파트

# 함수화 하기
def naver_crawling(title_list, URL):
    driver=webdriver.Chrome('chromedriver.exe')
    driver.get(URL)

    img_list=[] 
    artist_list=[] 
    genre_list=[] 
    score_list=[]  
    story_list=[] 

    for i in range(len(title_list)):

        time.sleep(0.5)

        # 제목에 해당하는 엘리먼트 클릭 순서대로 클릭
        page=driver.find_elements_by_class_name('title')
        page[i].click()

        time.sleep(0.01)

        #셀레니움으로 열어서 페이지 정보 가져오기
        html = driver.page_source
        soup = bs(html,'html.parser')

        #작품 썸네일 이미지
        img=soup.select('#content > div.comicinfo > div.thumb > a > img')[0]['src']
        img_list.append(img)

        #작가님 닉네임 수집
        artist = soup.select('#content > div.comicinfo > div.detail > h2 > span.wrt_nm')
        artist_list.append(artist[0].string.strip())

        #줄거리 링크 
        story=soup.select('#content > div.comicinfo > div.detail > p:nth-child(2)')
        story_list.append(story[0].get_text())

        #작품 장르 수집
        genre = soup.select('#content > div.comicinfo > div.detail > p.detail_info > span.genre')
        genre_list.append(genre[0].string)

        # 최신 별점 평균 점수 수집 (최대 10화 분량) : 이부분은 참조함
        # https://prod.velog.io/@2taesung/wt.gg-%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%9B%B9%ED%88%B0-%ED%81%AC%EB%A1%A4%EB%A7%81
        score = soup.find_all('strong')

        scorelist=[] ; ii=9
        while score[ii].text[0].isnumeric()==True:
            scorelist.append(float(score[ii].text))
            ii +=1
            if len(scorelist) == 10:
              break
        score_list.append(sum(scorelist)/len(scorelist))

        time.sleep(0.5)

        driver.back()
        
        time.sleep(0.2)
        
        page.clear()
        
        time.sleep(0.01)
        
        #데이터 프레임으로 변환
        df = pd.DataFrame(zip(title_list, artist_list, genre_list, score_list, story_list,img_list, link_list), 
                             columns = ['Title', 'Artist', 'Genre', 'Score(recent 10)', 'Story', 'Image', 'Link'])
    return df

# 연재중 웹툰 크롤링
URL = 'https://comic.naver.com/webtoon/weekday.nhn'
html = requests.get(URL).text # html 문서 전체를 긁어서 출력해줌, .text는 태그 제외하고 text만 출력되게 함
soup = bs(html, 'html.parser')

# 링크와 제목 가져오기
link_list = []
title_list = []

# 각 숫자 1~7까지는 월화수목금토일을 의미한다.
for i in range(1,8): 
    tl_tag=soup.select(f'#content > div.list_area.daily_all > div:nth-child({i}) > div > ul > li > a')
    
    #각 요일의 각 웹툰들에 해당하는 주소와 제목을 가져온다.
    for j in range(len(tl_tag)): 
        title = tl_tag[j]['title']
        link = tl_tag[j]['href']
        title_list.append(title)
        link_list.append(f'https://comic.naver.com{link}')

# 가져온 제목 리스트를 이용하여 함수 돌리기
URL='https://comic.naver.com/webtoon/weekday.nhn'
df_yonjae  = naver_crawling(title_list, URL)

# 결과물 csv로 저장하기
df_yonjae.to_csv('naver_webtoon_real.csv', index=False)


# 완결 네이버 웹툰 정보 크롤링 파트

# 함수화 하기
def naver_crawling_finish(title_list, URL):
    driver=webdriver.Chrome('chromedriver.exe')
    driver.get(URL)
    
    img_list=[] 
    artist_list=[] 
    genre_list=[] 
    score_list=[]  
    story_list=[] 

    for i in tqdm(range(1,1283)):
        page = driver.find_elements_by_class_name('thumb')
        
        time.sleep(0.5)

        # 제목에 해당하는 엘리먼트 클릭 순서대로 클릭
        page[i].click()

        time.sleep(0.01)

        #셀레니움으로 열어서 페이지 정보 가져오기
        html = driver.page_source
        soup = bs(html,'html.parser')

        #작품 썸네일 이미지
        img=soup.select('#content > div.comicinfo > div.thumb > a > img')[0]['src']

        img_list.append(img)

        #작가님 닉네임 수집
        artist = soup.select('#content > div.comicinfo > div.detail > h2 > span.wrt_nm')
        artist_list.append(artist[0].string.strip())

        #줄거리 링크 
        story=soup.select('#content > div.comicinfo > div.detail > p:nth-child(2)')
        story_list.append(story[0].get_text())

        #작품 장르 수집
        genre = soup.select('#content > div.comicinfo > div.detail > p.detail_info > span.genre')
        genre_list.append(genre[0].string)

        # 최신 별점 평균 점수 수집 (최대 10화 분량) : 이부분은 참조함
        # https://prod.velog.io/@2taesung/wt.gg-%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%9B%B9%ED%88%B0-%ED%81%AC%EB%A1%A4%EB%A7%81
        score = soup.find_all('strong')

        scorelist=[] ; ii=9
        while score[ii].text[0].isnumeric()==True:
            scorelist.append(float(score[ii].text))
            ii +=1
            if len(scorelist) == 10:
              break
        score_list.append(sum(scorelist)/len(scorelist))

        time.sleep(0.5)

        driver.back()

        time.sleep(0.2)

        page.clear()

        time.sleep(0.01)
        
    df = pd.DataFrame(zip(artist_list, genre_list, score_list, story_list,img_list), 
                      columns = ['Artist', 'Genre', 'Score(recent 10)', 'Story', 'Image'])
    return df

# 완결 웹툰 크롤링하기
URL = 'https://comic.naver.com/webtoon/finish'
html = requests.get(URL).text # html 문서 전체를 긁어서 출력해줌, .text는 태그 제외하고 text만 출력되게 함
soup = bs(html, 'html.parser')

# 링크와 제목 가져오기
link_list = []
title_list = []

for i in tqdm(range(1,1283)): #완결 웹툰 가장 마지막 인덱스(현재는 크롤링 날짜 기준)
    tl_tag=soup.select(f'#content > div.list_area > ul > li:nth-child({i}) > dl > dt > a')
    title = tl_tag[0]['title']
    link = tl_tag[0]['href']
    
    title_list.append(title)
    link_list.append(f'https://comic.naver.com{link}')

# 뽑아온 정보 데이터 프레임화 시키기
df_final_tl = pd.DataFrame(zip(title_list,link_list), columns = ['Title', 'Link'])

# 제목 리스트를 이용하여 함수 돌리기
df_finish = naver_crawling_finish(title_list, URL)

# 데이터 프레임으로 변환하고 csv로 저장하기
df_finish.to_csv('naver_webtoon_finish_without_tl.csv', index=False)
df_final_etl = pd.read_csv('naver_webtoon_finish_without_tl.csv')

# 데이터 프레임 합치고 연재중 췝툰 csv와 변수 순서 맞추기
df = pd.concat([df_final_tl,df_final_etl],axis=1, join='inner') 
df=df[['Title', 'Artist', 'Genre', 'Score(recent 10)', 'Story', 'Image', 'Link']]
df.to_csv('naver_webtoon_finish.csv', index=False)

# 네이버 웹툰 회차별 썸네일 크롤링 하기
df1 = pd.read_csv('naver_webtoon_real.csv')
df2 = pd.read_csv('naver_webtoon_finish.csv')

df = pd.concat([df1,df2], ignore_index=True)

# 함수화 하기
# 함수 만들기

def bring_thumb_images(df):
    imglist = []
    cnt=1
    for i in tqdm(range(len(df))):
        
        print(df['Title'][i], '수집 중')
        
        # 웹툰의 각 회차별 썸네일 가져오기
        page = 1
        imgSrc=[]
        while True:
            url = df['Link'][i]+f"&page={str(page)}"
            res = requests.get(url)
            soup = bs(res.text, 'lxml')

            viewList = soup.select('.viewList tr')


            for view in viewList[3:]: # 배너 제외
                imgSrc.append(view.select_one('a > img').attrs.get('src'))
                cnt += 1
            time.sleep(0.01)

            if soup.select_one('a.next') == None:
                print('last page was ' + str(page))
                print(f'1830 중 {i+1} 완료')
                break
            page = page + 1
            time.sleep(0.01)
        
        #위에서 만들어진 리스트를 원하는 형태로 바꾸어 하나의 리스트로 담아주기
        img_str = " π ".join(imgSrc)
        imglist.append(img_str)
    
    print(cnt)
    
    return imglist

img = bring_thumb_images(df)

df_thumb = pd.DataFrame({'Thumbs': img })
df_thumb.to_csv('naver_webtoon_thumbs.csv', index=False)

df = pd.concat([df, df_thumb], axis=1)
df.to_csv('naver_webtoon_all_with_thumbs.csv', index=False)