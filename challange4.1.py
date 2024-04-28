import pandas as pd 
import matplotlib.pyplot as plt 

data={'Title':['The Shawshank Redemption','The Godfather','The dark knight','12 Angry men','Schinderella','pulp fiction','Harry potter'],'Genre':['Drama','Crime','Action','Drama','Drama','crime','Fantasy']}

df=pd.DataFrame(data)
movies_count=df['Genre'].value_counts()

plt.figure(figsize=(4,5))
plt.bar(movies_count.index,movies_count)
plt.xlabel('Genre')
plt.ylabel('Frequncy')
plt.title('Number of movies by genre')
plt.show()