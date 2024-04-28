import pandas as pd 
import matplotlib.pyplot as plt 

data={'Plant Name':['Plant A','Plant B','Plant C','Plant D'],'Growth Stage':['Seedling','Sprout','Vegetative','Flowering']}

df=pd.DataFrame(data)
trees_count=df['Growth Stage'].value_counts()

plt.figure(figsize=(4,5))
plt.bar(trees_count.index,trees_count)
plt.xlabel('Growth Stage')
plt.ylabel('frequency')
plt.title('Distribution of plants')
plt.show()