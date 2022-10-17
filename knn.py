import pandas as pd
import numpy as np
dataframe=pd.read_csv("history.csv")

x=np.array(dataframe['hours']).reshape(-1,1)
y=np.array(dataframe['device']).reshape(-1,1)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x,y)

trained=pd.read_csv("trained.csv")
for i in range(len(trained)):
    xtest=np.array(trained["hours"][i]).reshape(-1,1)
    predicted= knn.predict(xtest) 
    trained["device"][i]=predicted
trained.to_csv("trained.csv",index=False)

