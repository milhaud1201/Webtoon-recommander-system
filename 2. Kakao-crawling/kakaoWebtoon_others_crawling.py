import pandas as pd
import json
import requests

def get_genre_url(code):
    genre_url = f"https://gateway-kw.kakao.com/decorator/v1/decorator/contents/{code}"
    headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko',
    'cookie': 'webid=7f21641f2bbd4c8f9af86d6a211be9d3; webid_ts=1653369352348; _kadu=siXZVdFTz5t_Qn9k_1657018568227; TIARA=E5LCJI_ZlE4MWqrCUUL8TobbA7yC.GcgRfwqr.8cXrnr8ayRx2IosGXe-cnpqd2c-KNtewZjukzYpK7qiyzafPuiGwrKxMOUYUxddSNEePo0; theme=dark; _kp_collector=KP.3859991296.1659595466116; _gcl_au=1.1.1256564681.1659595467; _fbp=fb.1.1659595467566.1992267394; _kptid=2606ff7d55eb4817b9f95bcae29fd01a; _gid=GA1.2.917645428.1659970395; _kawlt=p6AvPcB7VhEsx1uxoYSADKuWTbew1YZlkN2unHQOEy4FtqIFSZydN4IxZuUoggK3PjcN_R_5UFVSbU7dZGoS78YIDvLBvg7GIpoixDUJN95j_Wx3yZHpFZSIwCnwlkae; _kawltea=1660081117; _karmt=Hb7pXFTE3YJdAUu4iaHEHPvRrAwksBtbIanRjNiN0Ei749Lp55dsibfxpa0KS_od; _karmtea=1660091917; _kahai=ab97e19c37fa5fb1fae98fde30b632fb1d64e234f891aa4e8908a4655b95a265; _ga=GA1.2.529977311.1657242742; _ga_80D69HE0QD=GS1.1.1660101064.11.1.1660101254.0; _T_ANO=PuUBE4/x9cSNG6hqzYsH9GvBXc7Kfnh1X9Vb3KFFA7VdTpCU3P4qKQ/xtv/nHZpmQe1/SpOkioMZ8mT6NdhEYLjLsk0tqJw+dzkzRA4vC85qWEWMIfpSUBk+ulz+TTINl4fSPnGPCxnsGjOKiwVj5Rb8/d9A1HKMnkmWMVsa2uJpKHltLClx8KIZwZPRzzO6D7uW09feGswdWHVyf1G8CISZf5uLZDBJP7gJ86aPK25o1/gQJlgbo+Ch/Zyre2vRwdlazp7+fH6rUWjNnZnSf00WLpsArSnabmP2xMVhq3bHCqPhyKi3VvA5eatIYF/sK7PZYVocRQlr/4+U3KGNcA==',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    g_response = requests.get(genre_url, headers={"User-Agent": "Mozilla/5.0"})
    g_data = g_response.json()
    return g_data
    
def crawling_genre(code):

    g_data = get_genre_url(code)
    
    genre_list = []
    genre_list.append(g_data["data"]["genre"])
    return genre_list
  
def crawling_thumbnail(code):

    g_data = get_genre_url(code)

    thumbnail_list = []    
    thumbnail_list.append(g_data['data']["sharingThumbnailImage"] + '.webp')
    return thumbnail_list
  
def crawling_view(code):

    g_data = get_genre_url(code)

    view_list = []    
    view_list.append(g_data["data"]["statistics"]["viewCount"])
    
    return view_list
  
def crawling_like(code):

    g_data = get_genre_url(code)

    like_list = []
    like_list.append(g_data["data"]["statistics"]["likeCount"])
    
    return like_list
  
def gtlv(df):
    df['genre'] = df['id'].map(crawling_genre)
    df['thumbnail'] = df['id'].map(crawling_thumbnail)
    df['like'] = df['id'].map(crawling_view)
    df['view'] = df['id'].map(crawling_like)
    return df
