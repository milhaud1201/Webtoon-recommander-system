# Webtoon-recommender-system
📚한국 웹툰 추천 시스템(네이버, 카카오)
## 프로젝트 개요

월간 웹툰 이용자수가 8200만명 이상에 달한다고 합니다. [출처](https://www.upinews.kr/newsView/upi202205020041) 웹툰의 인기가 많아지는 만큼 작가들간의 경쟁도 심해지고, 독자는 원하는 웹툰을 찾기 어렵습니다. 저희 팀에서는 여러 플랫폼의 웹툰을 소개하고, 선호하는 장르, 그림체, 스토리 등을 고려한 사용자가 좋아할만한 웹툰을 추천해주는 시스템을 만들어 작가들에게는 홍보를, 독자들에게는 편의를 제공하려 합니다! 

## Project Maker

|  이세린  |  권소정  |  추창욱  |  박지현  |  김예림  |  음이레  |
|--------|--------|--------|--------|--------|--------|
| <img src='https://avatars.githubusercontent.com/u/105341794?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/105343406?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/107037722?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/108461149?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/105343281?v=4' height=80 width=80></img> | <img src='https://avatars.githubusercontent.com/u/92346855?v=4' height=80 width=80></img> 
| [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/srinlin) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/Kwon-Sojung) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/chuchacha) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/milhaud1201) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/yelimlikelion) | [![Git Badge](http://img.shields.io/badge/-Github-black?style=flat-square&logo=github)](https://github.com/yirehE) |


## 프로젝트 소개
* 그림체 추천
  ```
  어쩌구
  ```
  
* 장르 추천
  ```
  어쩌구
  ```
  
* 평점 추천
  ```
  어쩌구
  ```

_ _ _
## 프로젝트 progress
1. 데이터 수집
    * 웹툰의 기본 정보 데이터 크롤링(제목, 글 작가, 그림 작가, 장르, 평점, 줄거리, 대표 이미지, 링크, 좋아요수, 조회수, 연재상태 등)
    * 웹툰의 회차별 썸네일 데이터 크롤링
  
2. 데이터 전처리
    * 카카오 웹툰 랭킹 계산 (네이버 평점과 호환)
      - 카카오의 좋아요와 조회수를 이용하여 네이버의 평점과 같은 점수를 계산함
      - ```평점 계산 방법:웹툰의 랭킹 매기는 방법을 이용 (3 ~ 4일치의 누적 조회수가 높은순)```
      - ```카카오 웹툰의 3일치 누적 조회수를 계산하여 이를 토대로 네이버와 비슷한 분포로 평점을 부여```

    * 카카오 웹툰과 네이버 웹툰의 장르 통일
      * 
    ```
    **네이버**
    - 무협/사극 -> 무협
    - 옴니버스, 에피소드, 스토리 -> 삭제
    - 개그 -> 코믹
    - 무협/사극, 액션 -> 액션/무협
    - 스포츠 -> 학원
    - 감성 -> 드라마 

    **카카오**
    - 액션/무협 -> 무협
    - 코믹/일상 -> 코믹, 일상
    - 판타지 드라마 -> 판타지, 드라마
    - 공포/스릴러 -> 스릴러
    - 로맨스 판타지 -> 로맨스, 판타지  
    ```

    * 필요 없는 column drop
    * 이미지 데이터 분류 (이미지 Png파일 폴더 별로 추출 및 pca 진행)
  
3. 추천시스템 모델링

4. Streamlit 배포
  
_ _ _
## 데이터 수집

## 데이터 전처리

## 추천시스템 모델링

## streamlit 배포

_ _ _
## 프로젝트 결과

## 프로젝트 회고

## 프로젝트 참고자료
