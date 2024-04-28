import pandas as pd
import matplotlib.pyplot as plt
data={'Title':['Avengers','Spiderman','Ironman','Thor','Hulk'],'Genre':['Superhero','SuperHero','SuperHero','SuperHero','SuperHero' ]}
data=pd.DataFrame(data)
print(data)
plt.plot(data['Title'],data['Genre'])

plt.xlabel('Title')
plt.ylabel('Genre')
plt.title('Movie Genres')
plt.grid(True)
plt.show()


