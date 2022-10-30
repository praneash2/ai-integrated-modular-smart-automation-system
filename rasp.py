import requests
import time
import pandas as pd
from datetime import datetime
import  subprocess

my_secretautomatic="https://blr1.blynk.cloud/external/api/get?token=Kee705KRVkmgSXrQhxQZ6VBQQK29PN5p&v2"
my_secretu0="https://blr1.blynk.cloud/external/api/update?token=Kee705KRVkmgSXrQhxQZ6VBQQK29PN5p&v0=0"
my_secretu1="https://blr1.blynk.cloud/external/api/update?token=Kee705KRVkmgSXrQhxQZ6VBQQK29PN5p&v0=1"
#getting the time and device status
listen=1
data=[]
count=0
readdf=pd.read_csv("trained.csv")# this the the csv after training 

#use for converting pandas to dict
dic_readdf=readdf.to_dict('tight')
d=(dic_readdf['data'])
new=(dict(d))

while listen:
  now = datetime.now()

  current_hour = (now.strftime("%H"))
  current_min= (now.strftime("%M"))
  requestdata= requests.get("https://blr1.blynk.cloud/external/api/get?token=Kee705KRVkmgSXrQhxQZ6VBQQK29PN5p&v0")
  inp=int(requestdata.text)# get input from the raspberry pi // need to add gpio
  data.append([int(str(current_hour)+str(current_min)),inp])
  print(data)
  if int(current_hour)==17 and int(current_min)==50:
    print("yes")
    df=pd.DataFrame(data,columns=['hours','device'])
    df.to_csv("recorded.csv",index=False)
    subprocess.run("python csv_merge.py", shell = True)
    subprocess.run("python knn.py", shell = True)
  
  
  
  upload_data = int(str(current_hour) + str(current_min))

  temp = (new[upload_data])
  if (requests.get(my_secretautomatic)):
    print("in automatic mode")
    if temp == 0:
  
      updatedata = requests.get(my_secretu0)
    else:
      updatedata = requests.get(my_secretu1)
  else:
    print("In Manual mode")
  

  time.sleep(60)




print(df)
