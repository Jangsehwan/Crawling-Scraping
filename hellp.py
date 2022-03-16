import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    gu_name = gu['MSRSTE_NM']
    gu_mise = gu['IDEX_MVL']
    if gu_mise > 60 :
        print(gu_name,gu_mise)

# print(rjson['RealtimeCityAir']['row'][0]['NO2'])


# 파이썬은 tap이 중요
# 중괄호말고 :
# 파이썬은 라이브러리가 방대해해
# 가상환경이란 프로젝트별로 패키지를 담을 공구함
