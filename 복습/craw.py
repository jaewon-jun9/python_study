from google.colab import drive
import os
# drive.mount('/content/drive')
# os.mkdir("/content/drive/MyDrive/crolist")
# os.mkdir("/content/drive/MyDrive/result")
os.chdir("/content/drive/MyDrive/crolist/")
# !unzip -qq "/content/drive/MyDrive/크롤링주소목록.zip"
# os.listdir("/content/drive/MyDrive/crolist/")
import datetime
import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
import openpyxl
import time
import pandas as pd
def parsing(address): 
    result=["Na","","","",""]
    order_list=[]
    try:
        response = requests.get(address)
        soup = BeautifulSoup(response.content, 'html.parser')
        title=soup.find('div',{'class': 'article-head'})
        result[1]=title.find('h1').text
        result[2]=title.find('div',{'class':'info'}).text.replace("\n","").replace("최종수정일 : ","").replace(".","/")
        curation_order = soup.find('div',{'class': 'curation_order'})
        for i in curation_order.find_all('a'):
            order_list.append(i.text)
    except:
        try:
            err=soup.find('div',{'class': 'inner'})
            if "삭제되었거나 조회가 되지 않는 자료입니다." in err.text:
                result[0]="X"
                # print("삭제되었거나 조회가 되지 않는 자료입니다.",end=",")
        except:
            pass
    if result[1]!="":
        result[0]="O"
    if len(order_list)>0:
        result[3]="O"
        result[4]=order_list
    else:
        result[3]="X"
    return(result)
#     time.sleep(0.5)
def filein(filename):
  wb=openpyxl.load_workbook(filename)
  sheet = wb['Sheet1']
  data=pd.DataFrame(sheet.values)
  count=0
  count2=0
  data["10"]=""
  for i in data.iloc[:,4]:
      # print(i)
      result=parsing(i)
      # print(result)
      if result[0]=="Na":
          pass
      else:
          data.iloc[count,6:10]=result[0:4]
          data.iloc[count,10]=str(result[4])
      count=count+1
      count2=count2+1
      if count2==50:
        print(filename,end=",")
        print(count,end=",")
        print(datetime.datetime.now())
        count2=0
  from openpyxl.utils.dataframe import dataframe_to_rows
  wb2 = openpyxl.Workbook()
  ws2 = wb2.active
  for r in dataframe_to_rows(data, index=False, header=False):
      ws2.append(r)
  wb2.save('../result/'+filename.replace(".xlsx","-result.xlsx"))
for i in os.listdir("/content/drive/MyDrive/crolist/"):
  if i[-4:]=="xlsx":
    filein(i)
  else:
    pass


# function ClickConnect() {
#     var buttons = document.querySelectorAll("colab-dialog.yes-no-dialog paper-button#cancel"); 
#     buttons.forEach(function(btn) { 
#         btn.click(); 
#     }); 
#     console.log("1분마다 자동 재연결"); 
#     document.querySelector("colab-toolbar-button#connect").click(); 
# } 
# setInterval(ClickConnect,1000*60);
 
#  external_polymer_binary_l10n__ko.js?vrz=colab-20220916-060047-RC00_474777951:1628 
        
#        Recording uncaught error: TypeError TypeError: Cannot read properties of null (reading 'click')
