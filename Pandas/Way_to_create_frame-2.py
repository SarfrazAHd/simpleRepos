import pandas as pd

#creating dataframem using Dictionary
#data={'day':[1,2,3,4,5,6,7,],
#	  'Temperature':[35,23,43,56,14,49,34],
#	  'Windspeed':[6,7,8,10,12,15,16],
#	  'Event':['Rain', 'Sunny', 'Cloudy',
#	   'Snow','Rain', 'Sunny', "Rain"]}



#creating Dataframe using tuple list


data=[(1,35,6,"Rain"),( 2,23,7,'Sunny'),
(3,43,8,'Cloudy'),(4,56, 10,'Snow'),
(5,14,12,'Rain'),(6,49,15 ,'Sunny'),
(7,34,16,'Rain')]


df=pd.DataFrame(data, columns=['day','Temperature',
	'Windspeed','Event'])


print(df.head())


