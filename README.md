# Digital-NEWDEAL

뉴딜(New Deal)이란 1929년 대공황 때 미국 정부가 대규모 공공사업으로 일자리 창출해 대공황을 극복한 것을 말함!

우리 정부도 경제 위기 극복을 위해 한국판 뉴딜을 실시

[2020.07.14] 발표한지 얼마 안된 따끈따끈한 계획이란 말씀!

https://www.gov.kr/portal/ntnadmNews/2207711
(자세한건 이쪽에 있음 ㅎㅎ)

그럼 한국판 뉴딜은 무엇이 다른가???

1)토목 사업과 확연히 구별, 디지털 .그린 인프라 구축 

2)포스트 코로나 시대 미래  먹거리 창출의 토대 

3)저탄소 경제 .사회 전환을 위한 선도 

4)미래 핵심 인재양성을 위한 장기 투자 



뉴딜은  크게 디지털 뉴딜 과 그린뉴딜로 나뉩니당~

그 중에서  이번 프로젝트 계획을 세운건 '디지털 뉴딜'

온라인 소비, 원격근무 등 비대면화 확산 + 디지털 화는 국가 경쟁력의 핵심요소 +  한국의 강점인 ICT기반으로 디지털 초격차 확대 필요

==> 디지털 경제 가속화 경제 역동성 촉진

<<디지털 뉴딜의 목표>>

1.DNA 생태계 강화
K-사이버 방역 !!

데이터댐 / 5G.AI 융합 확산 /지능형 정부 


2.교육 인프라 디지털 전환

3.비대면 산업 육성

(교육) 온라인-오프라인 융합학습 (근무)스마트병원, 스마트 건강관리  (의료) 원격근무 정착.제도화  (비지니스) 온라인 시장 진출 +스마트화 

4.SOC 디지털화 

스마트 물류 /스마트 항만/ 스마트 산단 /스마트 시티 /지능형 도로 /홍수 관리 시스템

디지털 분야의 대표과제는 데이터 댐 /지능형 정부 /스마트 의료 인프라

------------------
 # 빅데이터를 활용한 마스크 수거함 최적 위치 선정
 
 ## 목차
 
 
 1. 분석 배경 및 목적
    - 주제 선정 배경
    - 분석 목적
 2. 분석 목표
 3. [데이터 분석](#3-데이터-분석)
    - [분석 기준 설정](#분석-기준-설정)
    - [데이터 추출 및 시각화](#데이터-추출-및-시각화)
    - 오버레이
    - 분석 방법 적용
 4. 분석 결과
    - 대구시 최종 분석 결과
    - 활용방안 및 한계
 5. 시사점 도출

 
 -------------------------
 
* 쥬피터 노트북으로 전부 작성되었습니다 *
### 3. 데이터 분석


#### 분석 기준 설정

![analysis_standard](https://user-images.githubusercontent.com/33755241/97140003-1f760800-179f-11eb-948e-f7d6d9be1f32.PNG)





#### 데이터 추출 및 시각화

##### step 1 대구시 동데이터와 지하철 데이터 입히기


```
//header 입력
import pandas as pd
import folium
import json
```


```
//대구시 지하철 데이터(공공데이터포털)
DeaguSub = pd.read_csv('data/mysubway.csv', index_col = 0,encoding='cp949')
DeaguSub.rename(columns={'stattion':'Station'}, inplace=True)
DeaguStation = DeaguSub[['Station', '위도', '경도']]
DeaguStation.head()
```


```
//대구 중심으로 folium map 생성
map_deagu = folium.Map(location=[35.8649155,128.5963041],tiles= 'CartoDB positron', zoom_start=12)
```


```
//대구 행정구역(동단위) 데이터 지도에 입히기
deagumap = open('data/namgu.json', 'r', encoding='utf-8').read()
deagumap = json.loads(deagumap)
folium.GeoJson(deagumap, name='json_data').add_to(map_deagu)

```



```
//대구 지도에 지하철 위치 찍기
for i in DeaguStation.index:
    sub_lat =  DeaguStation.loc[i,'위도']
    sub_long = DeaguStation.loc[i,'경도']
    
    title = DeaguStation.loc[i,'Station']
    
    #지도에 데이터 찍어서 보여주기
    folium.Circle([sub_lat,sub_long],tooltip = title, color='#000000', fill='crimson', radius = 50).add_to(map_deagu)

//한글깨짐때문에 html로 저장
map_deagu.save('station.html')

```


##### step2 '남구'기준으로 인구분석

- 남구를 기준으로 json 파일 가공.

```
df = pd.read_csv('data/남구.csv')
df['dong'] = df['dong'].astype('str')
```


```
geo_data = open('data/namgu.json', 'r', encoding='utf-8').read()

m = folium.Map(location=[35.8649155,128.5963041], zoom_start=10)

//folium의 choropleth를 이용하여 인구수 시각화
folium.Choropleth(
    geo_data=geo_data,
    data=df,
    columns=['dong','count'],
    key_on='feature.properties.adm_cd2',
    fill_color='BuPu',fill_opacity=0.7, line_opacity=0.5,
    legend_name='populations',
).add_to(m)

//시각화된 데이터 확인
m
```


