import pandas as pd 
import matplotlib.pyplot as plt 

data={'Employee':['John Smith','Jane Doe','Michael Lee','Alice Johnson'],'Years of Experience':[5,8,3,10],'Employee Salary':[75000,92000,58000,11000]} 

df=pd.DataFrame(data)


plt.figure(figsize=(4,5))
plt.hist(df['Employee Salary'],color='pink',edgecolor='black',bins=10)
plt.title( 'histogram of Employee Salary')
plt.xlabel('Employee Salary')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()



