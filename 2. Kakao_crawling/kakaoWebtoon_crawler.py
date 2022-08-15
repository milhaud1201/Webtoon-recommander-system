import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

"""
카카오 웹툰 크롤러는
웹툰원작 연재, 완결 작품
소설원작 연재, 완결 작품의
작품소개를
gateway url로 스크랩 할 수 있습니다.
"""


# 연재웹툰, gateway url
# page source에서 찾을 수 있음
def serialized(URL):
    rep = requests.get(URL)
    data = rep.json()

    id_list = []
    title_list = []
    author_list = []
    synopsis_list = []
    keywords_list = []

    # 각 숫자 1~7까지는 월화수목금토일을 의미한다.
    for i in range(7):

    # 각 요일의 각 웹툰들에 해당하는 웹툰의 수를 가져온다.
        page = len(data['data']['sections'][i]['cardGroups'][0]['cards'])

        for j in range(page):

            # 작품 페이지 id
            id = data['data']['sections'][i]['cardGroups'][0]['cards'][j]['content']['id']
            id_list.append(id)

            # 작품 제목
            title = data['data']['sections'][i]['cardGroups'][0]['cards'][j]['content']['title']
            title_list.append(title)

            # 작품 스토리 작가
            author = data['data']['sections'][i]['cardGroups'][0]['cards'][j]['content']['authors'][0]['name']
            author_list.append(author)

            # 줄거리 수집
            synopsis = data['data']['sections'][i]['cardGroups'][0]['cards'][j]['content']['synopsis']
            synopsis = synopsis.replace('\n', ' ')
            synopsis_list.append(synopsis)

            # 작품 키워드
            keywords = data['data']['sections'][i]['cardGroups'][0]['cards'][j]['content']['seoKeywords']
            keywords = [i.replace('#', '') for i in keywords]
            keywords_list.append(keywords)

    keywords_df = pd.DataFrame(keywords_list)        
    df = pd.DataFrame(zip(id_list, title_list, author_list, synopsis_list))
    df = pd.concat([df, keywords_df], axis=1)

    column_names = ['id', 'title', 'author', 'synopsis',
        'keywords_1', 'keywords_2', 'keywords_3', 'keywords_4']
    df.columns = column_names

    return df

# 완결웹툰의 페이지 수, gateway url
# page source에서 찾을 수 있음
def completed(page_num, URL):
    rep = requests.get(URL)
    json = rep.json()
    data = json['data']

    id_list = []
    title_list = []
    author_list = []
    synopsis_list = []
    keywords_list = []

    for page in range(page_num):

        # 작품 페이지 id
        id = data[0]['cardGroups'][0]['cards'][page]['content']['id']
        id_list.append(id)

        # 작품 제목
        title = data[0]['cardGroups'][0]['cards'][page]['content']['title']
        title_list.append(title)

        # 작품 스토리 작가
        author = data[0]['cardGroups'][0]['cards'][page]['content']['authors'][0]['name']
        author_list.append(author)

        # 줄거리 수집
        synopsis = data[0]['cardGroups'][0]['cards'][page]['content']['synopsis']
        synopsis = synopsis.replace('\n', ' ')
        synopsis_list.append(synopsis)

        # 작품 키워드
        keywords = data[0]['cardGroups'][0]['cards'][page]['content']['seoKeywords']
        keywords = [i.replace('#', '') for i in keywords]
        keywords_list.append(keywords)

    keywords_df = pd.DataFrame(keywords_list)
    df = pd.DataFrame(zip(id_list, title_list, author_list, synopsis_list))
    df = pd.concat([df, keywords_df], axis=1)

    column_names = ['id', 'title', 'author', 'synopsis', 'keywords_1', 'keywords_2', 'keywords_3', 'keywords_4']
    df.columns = column_names
            
    return df
