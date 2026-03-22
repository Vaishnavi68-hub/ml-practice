#DATA FRAMES 

#manually crrated data frame

import pandas as pd
std_data=[(1,'Ravi',32,'male','Nagpur'),
          (2,'Shivaji',33,'male','Pune'),
          (3,'Shreya',31,'female','mumbai')]

df=pd.DataFrame(std_data,columns=['roll_no','name','age','gender','city'])
print(df)

#imporing data from csv files

df=pd.read_csv('students.csv')
print(df)


#FUNCTIONS 

print(df.head()) #First 5 rows 

print(df.tail()) #Last 5 rows

print(df.shape) #no. of rows and columns

print(df.columns) #column names

print(df.Age) #age column 

print(df.size) #total no of elements in data frame

print(df.dtypes) #each coumn data type

print(df.values) #all values in data fmae in array form

print(df.index) #index of data frame 