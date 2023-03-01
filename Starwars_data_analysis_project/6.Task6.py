#Instructions:
#1. Use the df.sum() method to compute the sum of each seen columns.
#2. Make a bar chart of each ranking. You can use a matplotlib bar chart for this.
#3. Write up your thoughts on why the results look the way they do in a markdown cell. Also discuss 
#   how the results correlate with the rankings.
import matplotlib.pyplot as plt
import pandas as pd

starwars = pd.read_csv('StarWars4.csv', encoding="ISO-8859-1")
starwars['Have you seen any of the 6 films in the Star Wars franchise?'].fillna('NaN', inplace=True)
starwars['Do you consider yourself to be a fan of the Star Wars film franchise?'].fillna('NaN', inplace=True)
print(starwars)

labels = ['Ep 1', 'Ep 2', 'Ep 3', 'Ep 4', 'Ep 5', 'Ep 6']
#Using '.sum()' function works because the function treats boolean as values. (1 for True and 0 for False)
#If worried that strings values may affect the result of '.sum()', you can convert all the string values to 0 just in vase
values = [starwars['seen_ep1'].sum(), starwars['seen_ep2'].sum(), starwars['seen_ep3'].sum(), starwars['seen_ep4'].sum(), starwars['seen_ep5'].sum(), starwars['seen_ep6'].sum()]

plt.bar(labels, values)

plt.title('Bar Graph of views of each Star Wars movie')
plt.xlabel('Star Wars movie')
plt.ylabel('Views')

plt.yticks([0,100,200,300,400,500,600,700,800])

plt.savefig('bargraph_views_each_movie.png', dpi=100)

plt.show()



