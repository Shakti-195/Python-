import pandas as pd 
import matplotlib.pyplot as plt 

data={'Title':['The Shawshank Redemption','The GodFather','The Dark Knight','The GodFather: Part II','Pulp Fiction','The Lord Of the Rings:The Return of the King','Schindler\'s list','12 Angry Men','The Lord of the Rings:The FellowShip of the Ring'],'Genre':['Drama','Crime','Action ','Crime','Adventure','Historical Drama','Drama','Adventure','Drama']}

df=pd.DataFrame(data) 

plt.figure(figure=(3,5))
plt.bar(df['Title'],df['Genre'],color='red')
plt.title('Title Vs Genre')
plt.xlabel('Title')
plt.ylabel('Genre')
plt.grid(True)
plt.show()

