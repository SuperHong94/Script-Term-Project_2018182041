from bs4 import BeautifulSoup
import requests





def search(cityName):
    api = "https://openapi.gg.go.kr/RegionMnyFacltStus?"
    test = "KEY=2902618a276345c78da7557883182ca9"
    storeNames = []
    induTypes=[] # 업종명
    refine_roadNms=[] #도로명 주소
    telNums=[]#전화번호
    refine_zip_nums=[] # 우편번호
    lats=[] #위도
    logts=[] #경도

    resultLst = [] #검색결과
    for i in range(1,10):
        req=requests.get(api+test+"&pIndex="+str(i)+"&pSize=5&SIGUN_NM="+cityName)
        html=req.text
        soup=BeautifulSoup(html,"html.parser")
        if soup.findAll('code')=="INFO-200":
            break
        '''storeName=soup.findAll('cmpnm_nm')
        induType=soup.findAll('indutype_nm')
        refine_roadNm=soup.findAll('refine_roadnm_addr')
        telNum=soup.findAll('telno')
        refine_zip_num=soup.findAll('reffine_zip_cd')
        lat=soup.findAll('reffine_wgs84_lat')
        logt=soup.findAll('reffine_wgs84_logt')
        for n in storeName:
            storeNames.append(n.text)
        for n in induType:
            induTypes.append(n.text)

        for n in refine_roadNm:
            refine_roadNms.append(n.text)
        for n in telNum:
            telNums.append(n.text)
        for n in refine_zip_num:
            refine_zip_nums.append(n.text)
        for n in lat:
            lats.append(n.text)
        for n in logt:
            logts.append(n.text)'''

        r=soup.findAll('row')
        for n in r:
            print(n[0])
            resultLst.append(n.text)

    #print(len(storeNames)," ",len(induTypes)," ",len(refine_roadNms)," ",len(telNums)," ",len(refine_zip_nums)," ",len(lats)," ",len(logts))

     # [문자열정보,(위도,경도)]
    #for j in range(2):
       # resultLst.append((str(j+1)+'\t'+cityName+'\t'+storeNames[j]+'\t'+induTypes[j]+'\t'+refine_roadNms[j]+'\t'+telNums[j]+'\t'+refine_zip_nums[j]
         #                 ,(eval(lats[j]),eval(logts[j]))))

    print("검색완료")
    return resultLst

'''
for j in storeNames:
    print(j)'''



