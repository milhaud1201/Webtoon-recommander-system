# Webtoon-recommender-system
📚한국 웹툰 추천 시스템(네이버, 카카오)
## 프로젝트 개요

우리의 손에 들려있는 스마트폰으로 즐길 수 있는 가장 큰 즐거움 중 하나는 바로 **웹툰**이다. 한국콘텐츠진흥원에 따르면 웹툰은 10대부터 60대까지 다양한 연령대가 즐길 뿐만 아니라 여러 콘텐츠 시장에서의 경쟁력을 보이고 있다.
현재 국내에서 서비스되고 있는 웹툰은 네이버, 카카오 등 포탈을 중심으로 매우 빠른 성장을 보이고 있다. 
뿐만 아니라 국내 웹툰 플랫폼 중 하나인 네이버웹툰의 월간 전 세계 웹툰 이용자 수가 1억 8000만 명에 달한다고 한다. 웹툰의 인기가 많아지는 만큼 작가들 간의 경쟁도 심해지고, 독자는 원하는 웹툰을 찾기 어려워지고있다. 
웹툰 이용자를 대상으로 평소 웹툰 이용행태를 살펴보면 웹툰을 선택하는 가장 중요한 기준은 장르(52.5%)이며 그림체는(44.0%)로 높은 비중을 차지했다. 이에 따라 우리는 장르와 그림체를 기준으로 사용자가 좋아할 만한 웹툰을 추천해 주는 시스템을 만들어 작가들에게는 홍보를, 독자들에게는 편의를 제공하려 한다.

## Project Maker

|  이세린  |  권소정  |  추창욱  |  박지현  |  김예림  |  음이레  |
|--------|--------|--------|--------|--------|--------|
| <img src='https://avatars.githubusercontent.com/u/105341794?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/105343406?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/107037722?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/108461149?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/105343281?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/92346855?v=4' height=80 width=80></img> 
| [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/srinlin) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/Kwon-Sojung) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/chuchacha) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/milhaud1201) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/yelimlikelion) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/yirehE) |

_ _ _
## 프로젝트 process
1. 데이터 수집
2. 데이터 전처리
3. 장르기반 추천 시스템 모델링
4. 그림체 기반 추천시스템 모델링
5. 서비스 구현
_ _ _
## 프로젝트 내용
* 그림체 기반 추천
  ```
  어쩌구
  ```
  
* 장르 기반 추천
  ```
  선호하는 웹툰을 입력하면 유사한 장르 10개의 웹툰을 추천해 주는 시스템이다. 이때 다중 입력이 가능하다.
  웹툰별 장르의 유사성을 구하기 위하여 코사인 유사도를 사용하여 추천 시스템 모델링을 구현하였다. 
  같은 유사도를 가진 웹툰에 대해서는 평점이 더 높은 결과를 반환하도록 하며 총 10개의 웹툰을 추천해 준다.
  단, 유사도와 평점이 같은 웹툰은 랜덤으로 추천해 주는 작업을 진행하였다.
  ```

## 시연 영상

## 상세 내용
|  프로젝트명  |  Github  |  Paper  |  Notion  |  Presentation |
|-----------|-----------|-----------|-----------|-----------|
|장르 & 그림체기반 웹툰 추천 시스템|[Link](https://github.com/milhaud1201/Webtoon-recommender-system)|[pdf](Files/Webtoon-Recommender-System-Summary.pdf)|[Notion](https://rough-lan-909.notion.site/00ba82baeee64363bf8ddb60f0af09e9)|[YouTube]()|

## 프로젝트 참고자료 및 출처
* korean webtoon recommendation system (Naver and Daum): [출처](https://github.com/eunxu-10/Recommendation-System)
* 콘텐츠의 특성과 사용자의 선호도를 고려한 웹툰 추천 시스템 : [출처](https://github.com/CUAI-CAU/Webtoon-Recommendation)
* 김영학 (2018) [마크로밀 트렌드 조사:웹툰] 만화를 양지로 끌어올린 웹툰, 생태계에 대한 관심 필요: [출처](https://www.startuptoday.kr/news/articleView.html?idxno=10395)
* 김해욱 (2022) ‘네이버웹툰, 분사 5년만에 월 이용자수·매출 4배 넘게 성장’ UPI뉴스기사: [출처](https://www.upinews.kr/newsView/upi202205020041)
* 한국콘텐츠진흥원 2021 만화·웹툰 이용자 실태조사: [출처](https://www.kocca.kr/kocca/bbs/view/B0000147/1846252.do?searchCnd=1&searchWrd=%EC%9B%B9%ED%88%B0&cateTp1=&cateTp2=&useYn=&menuNo=204153&categorys=0&subcate=0&cateCode=&type=&instNo=0&questionTp=&ufSetting=&recovery=&option1=&option2=&year=&morePage=&qtp=&domainId=&sortCode=&pageIndex=1)
* 양지훈, 이지영, & 이상우. (2016). 웹툰 (Webtoon) 의 흥행 결정요인 연구. *한국콘텐츠학회논문지*, 16(5), 194-204.
* 도상범, & 강주영. (2018). 한, 미, 일 웹툰 분석을 통한 구독자 선호 요인 탐색: 네이버 웹툰을 중심으로. *한국빅데이터학회지*, 3(1), 21-32.
* 최건호, 파이토치 첫걸음, 한빛미디어 2019

