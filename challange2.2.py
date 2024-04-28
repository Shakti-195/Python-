import pandas as pd 
import matplotlib.pyplot as plt 
data={'Origin City':['New York','Los Angeles','Paris','Dubai','Frankfurt'],'Destination City':['London','Tokyo','Beijing','Sydney','Singapore'],'Flight Distance(km)':[5575,8974,8563,12844,10621],'Travel Time(hrs)':[7.0,115,10.0,16.0,13.5]}

df=pd.DataFrame(data)

plt.figure(figsize=(4,5))
plt.scatter(df['Flight Distance(km)'],df['Travel Time(hrs)'])
plt.title('Flight Distance Vs Travel Time')
plt.xlabel('Flight Distance(km)')
plt.ylabel('Travel Time(hrs)')
plt.grid(True)
plt.show()