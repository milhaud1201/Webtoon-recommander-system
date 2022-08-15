import requests
import json
import time

# code = webtoon_id

def collect_thumbnail_img(code):
    timg_list = []
    url = f"https://gateway-kw.kakao.com/episode/v2/views/content-home/contents/{code}/episodes?sort=-NO&offset=0&limit=1000"
    
    ### url -> thumbnail image
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko',
    'cookie': 'webid=7f21641f2bbd4c8f9af86d6a211be9d3; webid_ts=1653369352348; _kadu=siXZVdFTz5t_Qn9k_1657018568227; TIARA=E5LCJI_ZlE4MWqrCUUL8TobbA7yC.GcgRfwqr.8cXrnr8ayRx2IosGXe-cnpqd2c-KNtewZjukzYpK7qiyzafPuiGwrKxMOUYUxddSNEePo0; theme=dark; _kp_collector=KP.3859991296.1659595466116; _gcl_au=1.1.1256564681.1659595467; _fbp=fb.1.1659595467566.1992267394; _kptid=2606ff7d55eb4817b9f95bcae29fd01a; _gid=GA1.2.917645428.1659970395; _kawlt=p6AvPcB7VhEsx1uxoYSADKuWTbew1YZlkN2unHQOEy4FtqIFSZydN4IxZuUoggK3PjcN_R_5UFVSbU7dZGoS78YIDvLBvg7GIpoixDUJN95j_Wx3yZHpFZSIwCnwlkae; _kawltea=1660081117; _karmt=Hb7pXFTE3YJdAUu4iaHEHPvRrAwksBtbIanRjNiN0Ei749Lp55dsibfxpa0KS_od; _karmtea=1660091917; _kahai=ab97e19c37fa5fb1fae98fde30b632fb1d64e234f891aa4e8908a4655b95a265; _ga=GA1.2.529977311.1657242742; _ga_80D69HE0QD=GS1.1.1660101064.11.1.1660101254.0; _T_ANO=PuUBE4/x9cSNG6hqzYsH9GvBXc7Kfnh1X9Vb3KFFA7VdTpCU3P4qKQ/xtv/nHZpmQe1/SpOkioMZ8mT6NdhEYLjLsk0tqJw+dzkzRA4vC85qWEWMIfpSUBk+ulz+TTINl4fSPnGPCxnsGjOKiwVj5Rb8/d9A1HKMnkmWMVsa2uJpKHltLClx8KIZwZPRzzO6D7uW09feGswdWHVyf1G8CISZf5uLZDBJP7gJ86aPK25o1/gQJlgbo+Ch/Zyre2vRwdlazp7+fH6rUWjNnZnSf00WLpsArSnabmP2xMVhq3bHCqPhyKi3VvA5eatIYF/sK7PZYVocRQlr/4+U3KGNcA==',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    rep = requests.get(url, headers=headers)
    timg_data = rep.json()
        
    timg_no = timg_data["data"]["episodes"][1]["no"]
    for i in range(timg_no):
        try: 
            timg_list.append(timg_data["data"]["episodes"][i]["asset"]["thumbnailImage"]+'.webp')
#             time.sleep(0.1)
        except IndexError:
            break
#     df_timg = pd.DataFrame({"id":[code], "timg":[timg_list]})
    return timg_list

#   kakaoWebtoon_crawler.py에서 크롤링한 DataFrame의 id에 map
