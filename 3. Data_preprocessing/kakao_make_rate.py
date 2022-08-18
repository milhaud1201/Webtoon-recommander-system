import os

import requests
from requests import Response

import pandas as pd

from time import sleep
from bs4 import BeautifulSoup

# 카카오톡 크롤링 함수 불러오기 (보통 랭크가 매겨지는 기준은 3~4일치 누적 조회수 이므로 이를 계산하기 위함)
def get_genre_url(code):
    genre_url = f"https://gateway-kw.kakao.com/decorator/v1/decorator/contents/{code}"
    g_response = requests.get(genre_url)
    g_data = g_response.json()
    return g_data

def crawling(code):
    """
    returns view, like, title when input webtoon id
    """
    g_data = get_genre_url(code)  
    view = int(g_data["data"]["statistics"]["viewCount"])
    like = int(g_data["data"]["statistics"]["likeCount"])
    title = g_data["data"]["title"]
    
    return view, like, title

df_kakao_webtoon = pd.read_csv('kakao_webtoon.csv')

view_df = []
like_df = []
title_df = []

for id in df_kakao_webtoon.id:
    view, like, title = crawling(id)
    view_df.append(view)
    like_df.append(like)
    title_df.append(title)

df_kakao_webtoon2 = pd.DataFrame({"Title": title_df, "Like" : like_df, "View": view_df})

import time
t = time.localtime()

df_kakao_webtoon2.to_csv("kakao_webtoon_{0:02d}{1:02d}.csv".format(t.tm_mon, t.tm_mday), index=False)

# 필요한 데이터 불러오기 및 전처리
# 앞으로 필요한 제목, 좋아요, 조회수만 가져오기
df_kakao_webtoon = df_kakao_webtoon[['title','like','view']]
df_kakao_webtoon['like'] = df_kakao_webtoon['like'].str.strip('['']').astype(int)
df_kakao_webtoon['view'] = df_kakao_webtoon['view'].str.strip('['']').astype(int)

df_kakao_webtoon.rename(columns ={'like' : 'view', 'view' : "like"}, inplace=True)

df_view_diff = df_kakao_webtoon2['View'] - df_kakao_webtoon['view']
df_view_diff.describe()

df_like_diff = df_kakao_webtoon2['Like'] - df_kakao_webtoon['like']
df_like_diff.describe()

df_diff = pd.DataFrame({"title": df_kakao_webtoon['title'], "view_diff": df_view_diff, "like_diff":df_like_diff})
del df_like_diff, df_view_diff

# 네이버 평점 데이터 불러오기
df_naver = pd.read_csv("naver_webtoon_final.csv")

df_naver["Score(recent 10)"].hist(figsize=(12,4), bins=30)

# 카카오에 있는 정보를 이용하여 네이버 평점과 비슷한 점수를 매기는 함수 만들기
# 네이버 평점별로 전체의 몇퍼센트를 차지하는지 확인
df_percent = df_naver.groupby("Score(recent 10)").count()[['Title']].div(df_naver.shape[0]).sort_values(ascending=False, by="Score(recent 10)")

# 중복 웹툰 제거 후 단기 조휘수 순으로 정렬
df_diff.drop_duplicates(subset=['title'],inplace=True)
df_diff = df_diff.sort_values("view_diff",ascending=False)

# 카카오 웹툰의 평점이 네이버 웹툰의 평점과 같은 분포를 가지게 점수를 부여한다
per_sum = 0
per_list = []
for per in df_percent.values:
    per_sum += per
    num = round(int(df_diff.shape[0]*per_sum))
    per_list.append(num)

per_list2 = []
for i in range(len(per_list)):
    
    if i == 0:
        per_list2.append(per_list[i])
    else:
        per_list2.append(per_list[i]-per_list[i-1])


kakao_score = []

for i in range(len(per_list)):
    for j in range(per_list2[i]):
        kakao_score.append(df_percent.index[i])
kakao_score.append(df_percent.index[-1])

df_diff['score']=kakao_score

# 카카오 데이터 프레임에 평점 합치기
df_diff['id'] = 0
for ind in df_diff.index:
    df_diff['id'][ind] = df_kakao_webtoon.id.loc[ind]

df_diff.to_csv('kakao_webtoon_scoring.csv', index=False)
