# 카카오와 네이버 통일된 최종 csv 만들기
import pandas as pd
import numpy as np
import re

df_naver = pd.read_csv('naver_webtoon_final.csv')
df_kakao_score = pd.read_csv('kakao_webtoon_scoring.csv')
df_kakao = pd.read_csv('kakao_webtoon.csv')

# 데이터 전처리 하기

# 카카오와 네이버 칼럼 규칙
'''
제목 -> title
작가(작가와 그림작가 합치기) -> artist
장르 -> genre
평점 -> score
줄거리 -> story
대표이미지 -> image
회차별 썸네일 -> thumbs
어느 플랫폼인지 -> from
'''

# 네이버 전처리
df_naver.drop('Link', axis=1, inplace=True)
df_naver.rename(columns = {'Title': 'title', 'Artist': 'artist', 'Genre': 'genre', 'Score(recent 10)': 'score', 'Story':'story', 'Image': 'image', "Thumbs": 'thumbs'}, 
                inplace=True)

# 카카오 전처리
df_kakao.drop(["id","original_story","keywords_1", "keywords_2", "keywords_3", "keywords_4","adult", "like", "view", "status"],
              axis=1, inplace=True)

df_kakao_score.drop(['view_diff', 'like_diff', 'id'], axis=1, inplace=True)

df_kakao = pd.merge(df_kakao,df_kakao_score, on='title', how='outer')

# 네이버의 작가 형식과 통일되도록 카카오의 작가 이름 파생변수를 만들기

artist=[]
for i in range(len(df_kakao)):
    if df_kakao['writer'][i] == df_kakao['illustrator'][i]:
        artist.append(df_kakao['writer'][i])
    else:
        artist.append(df_kakao['writer'][i] + "/" + df_kakao['illustrator'][i])

df_kakao['artist'] = artist
df_kakao.drop(['writer','illustrator'], axis=1, inplace=True)

# 칼럼 통일을 카카오 칼럼 이름 변경하기

df_kakao.rename(columns = {'synopsis': 'story', 'timg': 'thumbs', 'thumbnail': 'image'}, inplace=True)

#함수 만들기
# 각 데이터별 변수 순서 통일하기

df_naver = df_naver.reindex(columns=['title', 'artist', 'genre', 'score', 'story', 'image', 'thumbs'])
df_kakao = df_kakao.reindex(columns=['title', 'artist', 'genre', 'score', 'story', 'image', 'thumbs'])

# 네이버와 카카오에 각각 파생 변수 생성하기

df_naver["from"]="naver"
df_kakao["from"]="kakao"

# 네이버 장르를 통일된 장르로 변환하는 함수 만들기

def naver_genre_change(df):
    # 개그 -> 코믹, 스포츠 -> 학원, 무협/사극 -> 무협, 감성 -> 드라마 로 변경
    df.genre = df.genre.str.replace('개그', '코믹')
    df.genre = df.genre.str.replace('스포츠', '학원')
    df.genre = df.genre.str.replace('무협/사극', '무협')
    df.genre = df.genre.str.replace('감성', '드라마')
    df.genre
    # 장르들을 list에 넣어줌
    df.genre = df.genre.str.split(', ')
    # 스토리, 옴니버스, 에피소드 장르 삭제
    rm_set = ['스토리', '옴니버스', '에피소드']
    new_list = []
    for i in df.genre:
        new_list.append([a for a in i if a not in rm_set])
    df.genre = new_list
    return df

# 카카오 장르를 통일된 장르로 변환하는 함수 만들기

def kakao_genre_change(df):
    # 장르 양 옆에 있는 [' '] 삭제
    df.genre = df.genre.str.strip('['']''\'')
    # '공포/스릴러'를 '스릴러'로 변경
    df['genre'][df.genre == '공포/스릴러'] = '스릴러'
    # 장르 여러개인 경우를 각각의 장르로 분류하기 위해 장르를 list로 변환해서 넣어줌
    df.genre = df.genre.str.replace('/', ' ').str.split()
    return df

# 네이버와 카카오의 각 회차별 데이터에서 원하는 뽑아올 수 있는 원하는 csv 형태로 만들기

def make_thumbs_csv(df_naver, df_kakao):
    df_naver.drop_duplicates('title', inplace=True)
    df_kakao.drop_duplicates('title', inplace=True)
    
    df_kakao["thumbs"] = df_kakao["thumbs"].map(lambda x: re.sub('\[|\]|\'','',x))
    df_kakao["image"] = df_kakao["image"].map(lambda x: re.sub('\[|\]|\'','',x))
    
    df_kakao = df_kakao.drop(columns = ['image'])
    split = df_kakao.thumbs.str.split(',')
    split = split.apply(lambda x: pd.Series(x))
    split = split.stack().reset_index(level = 1, drop = True).to_frame("thumbs")
    df_kakao = df_kakao.merge(split, left_index=True, right_index=True, how ="left")
    
    df_naver = df_naver.drop(columns = ['image'])
    split = df_naver.thumbs.str.split('π')
    split = split.apply(lambda x: pd.Series(x))
    split = split.stack().reset_index(level = 1, drop = True).to_frame("thumbs")
    df_naver = df_naver.merge(split, left_index=True, right_index=True, how ="left")
    
    df_naver.drop(['thumbs_x'], axis=1, inplace=True)
    df_kakao.drop(['thumbs_x'], axis=1, inplace=True)
    
    df_naver.rename(columns={'thumbs_y': 'thumbs'}, inplace=True)
    df_kakao.rename(columns={'thumbs_y': 'thumbs'}, inplace=True)
    
    df_naver = df_naver.reindex(columns=['title', 'artist', 'genre', 'score', 'story', 'thumbs', 'from'])
    df_kakao = df_kakao.reindex(columns=['title', 'artist', 'genre', 'score', 'story', 'thumbs', 'from'])
    
    df_for_thumbs = pd.concat([df_kakao[['title', 'thumbs', 'from']], df_naver[['title', 'thumbs', 'from']]])
    
    df_for_thumbs.to_csv("webtoon_thumbs.csv", index=False)

make_thumbs_csv(df_naver, df_kakao)
naver_genre_change(df_naver)
kakao_genre_change(df_kakao)

# 최종적으로 사용할 csv로 만들기

df_total = pd.concat([df_naver,df_kakao])
df_total.reset_index(drop=True, inplace=True)
df_total.drop('thumbs', axis=1, inplace=True)
df_total.drop_duplicates('title', inplace=True)
df_total.to_csv("webtoon_total_final.csv", index=False)