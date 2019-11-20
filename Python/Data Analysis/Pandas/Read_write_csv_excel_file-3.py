import pandas as pd

df=pd.read_csv("C:\\Users\\Nizam\\Downloads\\school_grades_dataset.csv" )


#df=pd.read_csv("C:\\Users\\Nizam\\Downloads\\school_grades_dataset.csv",nrows=3 )

df.to_csv('new.csv', index=False, columns=["school","sex"])

#print(df)