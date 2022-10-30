import requests
import time
import pandas as pd
from datetime import datetime
import  subprocess
#getting the time and device status
listen=1
data=[]
count=0
readdf=pd.read_csv("trained.csv")# this the the csv after training 

while listen:
  now = datetime.now()
  current_hour = int(now.strftime("%H"))
  current_min= int(now.strftime("%M"))
  requestdata= requests.get("https://blr1.blynk.cloud/external/api/get?token=Kee705KRVkmgSXrQhxQZ6VBQQK29PN5p&v0")
  inp=int(requestdata.text)# get input from the raspberry pi // need to add gpio
  data.append([int(str(current_hour)+str(current_min)),inp])
  print(data)
  if current_hour==17 and current_min==50:
    print("yes")
    df=pd.DataFrame(data,columns=['hours','device'])
    df.to_csv("recorded.csv",index=False)
    subprocess.run("python csv_merge.py", shell = True)
    subprocess.run("python knn.py", shell = True)
  if count==1439:
    count=0  
  
  if(str(current_hour+current_min)==str(readdf['hours'][0]) ):   this is the actual thing that we need to do
    updatedata= requests.get(f"https://blr1.blynk.cloud/external/api/update?token=Kee705KRVkmgSXrQhxQZ6VBQQK29PN5p&v0={readdf['device'][count]}")
    print(readdf['hours'][count],readdf['device'][count])# we can use gpio output instead of this
  
  #print(readdf['hours'][count],readdf['device'][count])#want to do put count instead of 0
  
  
  count=count+1  
  time.sleep(60)




print(df)
