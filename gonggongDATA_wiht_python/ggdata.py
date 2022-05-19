'''
파일 위치 찾아주기!
os.chdir('Desktop\CODE\python\pythin_exam')

파이썬 과학 프로그래밍 프로젝트
1. 양평군의 년별 전력 사용량 그래프

'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

class yp_data_anal:                 #월별 데이터 집합
    def __init__(self, year, month, used):
        self.year = int(year)
        self.month = int(month)
        self.used = int(used)
    def toString(self):
         print('{}년 {}월 사용량 : {}'.format(self.year,self.month,self.used))
         
class yp_year_sumAnal:              #연도별 합계 구분 
    def __init__(self, data,year):
        self.year = year
        self.people = int(data['people'].sum()/len(data))
        self.used = int(data['used'].sum()/len(data))
        self.money = int(data['money'].sum()/len(data))
        self.avg = int(data['avg_money'].sum()/len(data))
    def toString(self):
        print("년도 : {}\n가구 수 : {}\n사용량 : {}\n요금 합계 평균 : {}\n평균 단가 : {}".format(self.year,self.people,self.used,self.money,self.avg))

def returnClass(data, loc, year):       #지역과 '년도'로 데이터 추출 => 한 년도 내 모든 데이터 종합 평균치
    row = data.loc[data.year == year]
    row = row.loc[row.locate == loc]
    target  = row.loc[row.what == '합계']
    return yp_year_sumAnal(target,year)
    
def yp_month_anal(data,loc,year,month,what):    #지역, '월', 용도 데이터 추출 => 한 년도 내 월
    row = data.loc[data.year == year]
    row = row.loc[row.month == month]
    row = row.loc[row.locate == loc]
    target  = row.loc[row.what == what]
    if len(target['month']) == 0:
        return yp_data_anal(-1,-1,-1)   #에러처리 (빈 값 존재 시)
    return yp_data_anal(target['year'],target['month'],target['used'])
    
tag = ["year","month","locate","what","people","used","money","avg_money"]
origin = pd.read_csv('elec_use_18to22.csv',names=tag,encoding='cp949')

#데이터 셋 
yp_data = []
yp_monthly_data = []#양평군 주택용
yp_monthly_data2 = []#양평군 산업용
yp_monthly_data3 = []#양평군 일반용
yp_monthly_data4 = []#양평군 농사용

for i in range(2018,2023):
    yp_data.append(returnClass(origin,"양평군", i))                    #연도별 데이터 종합
    
for i in range(1,13):
    yp_monthly_data.append(yp_month_anal(origin,"양평군", 2021,i,"주택용"))     #2021년도 양평군 월별 데이터 종합
    yp_monthly_data2.append(yp_month_anal(origin,"양평군", 2021,i,"산업용"))  
    yp_monthly_data3.append(yp_month_anal(origin,"양평군", 2021,i,"일반용"))
    yp_monthly_data4.append(yp_month_anal(origin,"양평군", 2021,i,"농사용"))
yp_monthly_data.pop(7)  #에러 체크 하드코딩! 
yp_monthly_data2.pop(7)
yp_monthly_data3.pop(7)
yp_monthly_data4.pop(7) #이렇게 하면 ㅠㅠ





plt.subplot(2, 1, 1)   
x = np.array([i.year for i in yp_data])
y = np.array([i.used for i in yp_data])//10000000    #전력 사용량
plt.bar(x, y)
plt.ylim(6,13)
plt.title("electricity usage")
plt.xlabel('year')
plt.ylabel('amount')

plt.subplot(2, 1, 2)
x = np.array([i.month for i in yp_monthly_data])    #월
y = np.array([i.used for i in yp_monthly_data])    #주택 사용량
plt.plot(x, y,label="house")
y = np.array([i.used for i in yp_monthly_data2])    #산업 사용량
plt.plot(x, y,label="industry")
y = np.array([i.used for i in yp_monthly_data3])    #일반 사용량
plt.plot(x, y,label="nomal")
y = np.array([i.used for i in yp_monthly_data4])    #농사 사용량
plt.plot(x, y,label="nongsa")
plt.xlabel('2021')
plt.ylabel('amount')
plt.legend()

plt.show()
