import pandas as pd 
import matplotlib.pyplot as plt 

data={'Date':['01-12-2023','02-12-2023','03-12-2023','04-12-2023','05-12-2023'],'Temperature(High)':[15,18,12,10,17]}

df=pd.DataFrame(data)

plt.figure(figsize=(4,5))
plt.plot(df['Date'],df['Temperature(High)'])
plt.title('Date Vs Temperature(High)')
plt.xlabel('Date')
plt.ylabel('Temperature(High)')
plt.grid(True)
plt.show()
