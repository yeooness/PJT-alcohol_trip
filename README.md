# 🍺알콜 트립
## 티미름
<img src="alcohol_trip.assets/Alcohol.png" alt="Alcohol" style="zoom: 50%;" />

<br>

[프로젝트 바로가기](https://immense-chamber-32005.herokuapp.com/)

## ✔️팀원 소개 및 역할

조장: 김다겸

> 백엔드, 헤로쿠 배포, 맵 기능, 검색 기능, 소셜로그인, 유저페이지 등 구현

조원: 김문경

> 백엔드, 크롤링, 좋아요, 식당 모델, 검색, 맵 기능 등 구현

조원: 이정섭

> 프론트엔드, template 레이아웃 및 디자인 구현

조원: 황여원

> 백엔드, 댓글, 좋아요, 리뷰, 별점 기능 등 구현

   <a href="https://github.com/kimdakyeom/alcohol_trip/graphs/contributors">    <img src="https://contrib.rocks/image?repo=kimdakyeom/alcohol_trip" />   </a>

<br>



## ✔️기간

221031 ~ 221107

<br>

## ✔️주제

> 맛집 정보 및 후기 공유 커뮤니티 서비스 👉 **술집 정보 및 후기 공유 커뮤니티**

<br>



## ✔️사용 기술

- HTML
- CSS
- JS
- Django
- Selenium
- Heroku

<br>



## ✔️기능(페이지) 설명

### 🧩목차

- 메인 페이지
- 검색 기능
- 디테일 페이지
- 회원정보 기능

<br>



### 🧩메인 페이지

#### 1. 좋아요 상위 8개 표시

![image-20221108005907263](alcohol_trip.assets/image-20221108005907263.png)

> 좋아요 수를 카운트해서 역순으로 정렬

<br>



#### 2. 검색 기능

![image-20221108005942957](alcohol_trip.assets/image-20221108005942957.png)

> 검색창에 '이자카야'라고 검색한다면?

![image-20221108011357406](alcohol_trip.assets/image-20221108011357406.png)

<br>



#### 3. 실시간 검색어 순위

![image-20221108011439080](alcohol_trip.assets/image-20221108011439080.png)

<br>



### 🧩검색 기능(카테고리, 지역별)

#### 1. 카테고리 및 지역별로 검색

![image-20221108011742607](alcohol_trip.assets/image-20221108011742607.png)

![image-20221108011753030](alcohol_trip.assets/image-20221108011753030.png)

<br>



### 🧩디테일 페이지

#### 1. 수많은 정보들은 어떻게?

네이버 지도 페이지를 **Selenium** 라이브러리를 사용해서 크롤링

> 각 주점의 주소, 카테고리, 전화번호, 영업시간 등을 가져옴

❓왜 셀레니움을 사용했는가

> **Beautifulsoup**를 사용하면 네이버 영화 페이지나 멜론 페이지와 같은 **정적 페이지**는 가능
>
> 그러나, 동적으로 사이트를 이동하면서 데이터를 긁어오려면 **셀레니움**을 사용해야함!!

<br>



#### 2. 리뷰 및 댓글

**리뷰 작성 기능**과 각 리뷰에 대한 **댓글 작성 기능** 구현

![image-20221108011935290](alcohol_trip.assets/image-20221108011935290.png)

![image-20221108011920514](alcohol_trip.assets/image-20221108011920514.png)

> 리뷰 작성 기능

![image-20221108012000026](alcohol_trip.assets/image-20221108012000026.png)

![image-20221108012027462](alcohol_trip.assets/image-20221108012027462.png)

> 각 리뷰에 대해서 댓글 작성 가능
>
> 댓글 작성은 모달로 구현

<br>



#### 3. 좋아요 기능

사용자는 **음식점에 대한 좋아요**와 **사용자 리뷰**에 대한 좋아요가 가능

![image-20221108012211611](alcohol_trip.assets/image-20221108012211611.png)

![image-20221108012229472](alcohol_trip.assets/image-20221108012229472.png)

> 각각 음식점 및 리뷰에 대한 좋아요 기능

⭐**Javascript**를 활용한 **비동기 처리 구현**

<br>



#### 4. 기타

**상세지도** 부분을 통해 쉽게 위치 파악이 가능

![image-20221108012405570](alcohol_trip.assets/image-20221108012405570.png)

**네이버 플레이스 바로가기**를 통해 활용성 ⬆️

![image-20221108012416968](alcohol_trip.assets/image-20221108012416968.png)

<br>



### 🧩회원정보 기능들

#### 0. 유저 페이지

![image-20221108012502046](alcohol_trip.assets/image-20221108012502046.png)

#### 1. 소셜 로그인 기능

![image-20221108012528806](alcohol_trip.assets/image-20221108012528806.png)

기존 로그인 기능 + **네이버 및 카카오 로그인 기능 추가**

<br>



#### 2. 팔로워/팔로잉 기능

![image-20221108012551257](alcohol_trip.assets/image-20221108012551257.png)

![image-20221108015009732](alcohol_trip.assets/image-20221108015009732.png)

> 각 유저별로 팔로워/팔로잉이 누구인지 파악이 가능 

<br>



#### 3. 사용자 활동 내역

![image-20221108012558756](alcohol_trip.assets/image-20221108012558756.png)

> 각 활동마다 링크를 걸어서 쉽게 이동이 가능

<br>
