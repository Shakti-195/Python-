import numpy as np
a={'roll':np.arange(1,51),'marks':np.random.randint(100,size=50)}
print(a)
import pandas as pd 
df=pd.DataFrame(a)
print(df)
import matplotlib.pyplot as plt 
plt.hist(df['marks'],bins=10,edgecolor='black')
plt.xlabel('marks')
plt.ylabel('frequency')
plt.title('Distribution')
plt.grid(True)
plt.show()
