'''
원본 오픈 데이터에서 필요한 범위의 데이터를 추출하는 프로그램
공공데이터 출처
https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&sortColumn=&sortDirection=&infId=4Z9SGF03FTIIXU9IQNQE26457615&infSeq=1&searchWord=%EC%A0%84%EB%A0%A5
'''
import csv
import os

#os.chdir('Desktop\CODE\python\pythin_exam')


f = open('elec_use.csv', 'r', encoding='cp949')
f2 = open('elec_use_18to22.csv', 'w')
rdr = csv.reader(f)
wr = csv.writer(f2)
cnt = 0
for item in rdr:
    if cnt == 0:
        cnt+=1
        continue
    if(len(item)!=0 and int(item[0])>=2018):
        wr.writerow(item)

f.close()   