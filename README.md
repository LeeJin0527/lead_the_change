

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


