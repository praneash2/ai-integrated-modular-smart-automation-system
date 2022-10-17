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
  inp=1# get input from the raspberry pi // need to add gpio
  if current_hour==00 and current_min==0:
    subprocess.run("python csv_merge.py", shell = True)
    subprocess.run("python knn.py", shell = True)
    
  data.append([int(str(current_hour)+str(current_min)),inp])
  print(readdf['hours'][0],readdf['device'][0])# we can use gpio output instead of this
  
  if count==1:
    break
  count=count+1  
  time.sleep(3)

df=pd.DataFrame(data,columns=['hours','device'])

df.to_csv("recorded.csv",index=False)
print(df)
