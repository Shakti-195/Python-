import pandas as pd 
import matplotlib.pyplot as plt 

data={'Customer Id':[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],'Customer Age':[25,32,48,19,65,28,52,35,18,70]}

df=pd.DataFrame(data)
purchase_count=df['Customer Age'].value_counts()

plt.figure(figsize=(4,5))
plt.bar(purchase_count.index,purchase_count)
plt.xlabel('Customer Age')
plt.ylabel('Frequency')
plt.title('Purchase Frequency by  Age Group')
plt.show()