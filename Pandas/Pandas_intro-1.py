import pandas as pd

# df=pd.read_csv("C:\\Users\\Nizam\\Downloads\\school_grades_dataset.csv")

# print(df.shape())
# print(df.head())

weather_data = {'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017'],
                'Temperature': [32, 35, 36, 45, 40, 50],
                'Windspeed': [6, 7, 2, 3, 5, 10],
                'event': ["Rain", "sunny", "snow", "rain", "rain", "sunny"]}

df = pd.DataFrame(weather_data)
# print(df)

# print(df.head())

# print(df.tail(2))

# print(df[2:5])

# print(type(df['Temperature']))

# print(df[['day', "Temperature"]])

# x=df['Temperature']
# print("Mean of the Temperature is ",x.mean())

#print(df.describe())
print(df.info())

# print(df['Temperature']==df['Temperature'].max())
