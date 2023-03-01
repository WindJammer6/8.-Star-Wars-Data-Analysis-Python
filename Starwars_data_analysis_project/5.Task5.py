#Instructions:
#1. Use the pandas.DataFrame.mean() method to compute the mean of each ranking columns from the previous screen.
#2. Make a bar chart of each seen. You can use a matplotlib bar chart for this.
#3. Write up a summary of what you've done so far in a markdown cell. Also discuss why you think the respondents ranked the movies the way they did.
import matplotlib.pyplot as plt
import pandas as pd

starwars = pd.read_csv('StarWars4.csv')
starwars['Have you seen any of the 6 films in the Star Wars franchise?'].fillna('NaN', inplace=True)
starwars['Do you consider yourself to be a fan of the Star Wars film franchise?'].fillna('NaN', inplace=True)
print(starwars)

labels = ['Ep 1', 'Ep 2', 'Ep 3', 'Ep 4', 'Ep 5', 'Ep 6']
values = [starwars['rank1'].mean(), starwars['rank2'].mean(), starwars['rank3'].mean(), starwars['rank4'].mean(), starwars['rank5'].mean(), starwars['rank6'].mean()]

plt.bar(labels, values)

plt.title('Bar Graph of Ranking of each Star Wars movie by surveyed population \n (lower ranking, the better the movie)')
plt.xlabel('Star Wars movie')
plt.ylabel('Ranked (lower rank, the better the movie)')

plt.yticks([0,1,2,3,4,5])

plt.savefig('bargraph_rank_each_movie.png', dpi=100)

plt.show()


