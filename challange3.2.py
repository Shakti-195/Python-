import pandas as pd 
import matplotlib.pyplot as plt 
data={'Origin City':['New York','Los Angeles','Paris','Dubai','Frankfurt'],'Destination City':['London','Tokyo','Beijing','Sydney','Singapore'],'Flight Distance(km)':[5575,8974,8563,12844,10621]}

df=pd.DataFrame(data)

plt.figure(figsize=(4,5))
plt.hist(df['Flight Distance(km)'],bins=10,color='skyblue')
plt.title('histogram flight distance')
plt.xlabel('Flight Distance(km)')
plt.ylabel('frequency')
plt.grid(True)
plt.show()