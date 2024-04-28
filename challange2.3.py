import pandas as pd 
import matplotlib.pyplot as plt 

data={'Employee':['John Smith','Jane Doe','Michael Lee','Alice Johnson'],'Years of Experience':[5,8,3,10],'Employee Salary':[75000,92000,58000,11000]} 

df=pd.DataFrame(data)


plt.figure(figsize=(4,5),)
plt.scatter(df['Years of Experience'],df['Employee Salary'],color='green')
plt.title('Years of Experience Vs Employee Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Employee Salary')
plt.grid(True)
plt.show()



