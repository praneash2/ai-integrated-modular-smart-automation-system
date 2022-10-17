import pandas as pd
df=pd.read_csv("history.csv",index_col=False)
df1=pd.read_csv("recorded.csv")
df3 = pd.concat([df, df1], ignore_index = True)
df.reset_index()
df3.to_csv("history.csv",index=False)
print(df)

