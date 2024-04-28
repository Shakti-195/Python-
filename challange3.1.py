import pandas as pd 
import matplotlib.pyplot as plt 

data={'Country':['Japan','Switzerland','Singapore','Australia','Iceland'],'Life Expectancy':[84.3,84.2,83.7,82,83.3]}

df=pd.DataFrame(data)
plt.figure(figsize=(4,5))
plt.hist(df['Life Expectancy'],bins=10,color='green',edgecolor='black')
plt.title('histogram of Life Expectancy')
plt.xlabel('Life Expectancy')
plt.ylabel('frequency')
plt.grid(True)
plt.show()