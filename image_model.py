
import pandas as pd
import numpy as np
from math import dist

df_euclidien_distance = pd.read_csv('Euclidean_distanc_v2.csv', index_col='Unnamed: 0')
raw_total_df = pd.read_csv('webtoon_total_final.csv')
total_df = pd.read_csv('webtoon_total_final.csv')

df_euclidien_distance.shape

# # 불러온 데이터 전처리
total_df = total_df[['title', 'genre', 'score']]


def single_distance(title):
    similar_df =df_euclidien_distance[[title]]
    similar_df.columns = ['title']
    return similar_df

# 스타일 loss 값 저장한 csv에서 불러오는 부분
title_list = df_euclidien_distance.index.tolist()


def image_recommendation(title_input=[]):
    if title_input == []:
        return '웹툰을 선택해주세요'
    
    # result 데이터 프레임 만들기
    empty_list = [0 for i in range(len(df_euclidien_distance))]
    result = pd.DataFrame()
    result['result'] = empty_list
    result.index = title_list
    
    for title in title_input:
        tmp = single_distance(title)
        result['result'] = result.values + tmp.values
        
    result.sort_values('result',inplace=True)
    result.drop(title_input, inplace=True)
    
    result_title_list = result[:10].index.tolist()
    
    final_df = pd.DataFrame(columns=['title', 'artist', 'genre', 'story','image', 'score','from'])
    
    for r in result_title_list:
        tmp = raw_total_df[raw_total_df['title']== r]
        tmp = tmp[['title', 'artist', 'genre', 'story','image', 'score', 'from']]
        final_df = pd.concat([final_df,tmp])

    return final_df











