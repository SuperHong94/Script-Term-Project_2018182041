from bs4 import BeautifulSoup
import requests

cityName="부천시"
api="https://openapi.gg.go.kr/RegionMnyFacltStus?"
test="KEY=2902618a276345c78da7557883182ca9"

storeNames=[]

for i in range(1,100):
    req=requests.get(api+test+"&pIndex="+str(i)+"&pSize=500&SIGUN_NM="+cityName)
    html=req.text
    soup=BeautifulSoup(html,"html.parser")
    if soup.findAll('code')=="INFO-200":
        break
    storeName=soup.findAll('cmpnm_nm')
    for n in storeName:
        print(n)
        storeNames.append(n.text)

'''
for j in storeNames:
    print(j)'''



