import pandas as pd 
import matplotlib.pyplot as plt 

data={'Country':['Japan','Switzerland','Singapore','Australia','Iceland'],'Life Expectancy':[84.3,84.2,83.7,82.8,63.3],'GDP per capita':[39522,87169,65870,51408,67004]}

df=pd.DataFrame(data)

plt.figure(figsize=(4,5))
plt.scatter(df['GDP per capita'],df['Life Expectancy'],color='red')
plt.title('GDP per capita vs Life Expectancy')
plt.xlabel('GDP per capita')
plt.ylabel('Life Expectancy')
plt.grid(True)
plt.show()

