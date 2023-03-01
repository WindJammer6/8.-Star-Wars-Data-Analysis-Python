#Instructions:
#a. Do you consider yourself to be a fan of the Star Wars film franchise? — True or False
#b. Do you consider yourself to be a fan of the Star Trek franchise? — Yes or No
#c. Gender — Male or Female

#1. Split the data into two groups based on one of the binary columns above.
#2. Redo the two previous analyses (find the most viewed movie and the highest-ranked movie) separately for each group, and then compare the results.
#3. If you see any interesting patterns, write about them in a markdown cell.

#I will be attempting for option b, to see if being a fan of the Star Trek franchise affect if they rank the
#movies differently
import matplotlib.pyplot as plt
import pandas as pd

starwars = pd.read_csv('StarWars4.csv', encoding="ISO-8859-1")
starwars['Have you seen any of the 6 films in the Star Wars franchise?'].fillna('NaN', inplace=True)
starwars['Do you consider yourself to be a fan of the Star Wars film franchise?'].fillna('NaN', inplace=True)

a = starwars['Do you consider yourself to be a fan of the Star Trek franchise?']

starwars.loc[a == 'Yes', 'Do you consider yourself to be a fan of the Star Trek franchise?'] = True
starwars.loc[a == 'No', 'Do you consider yourself to be a fan of the Star Trek franchise?'] = False
a.fillna('NaN', inplace=True)

#We can split a DataFrame into two groups based on a binary column by creating two subsets of that column.
watched_st = starwars[a == True]
notwatched_st = starwars[a == False]

#labels = ['Ep 1', 'Ep 2', 'Ep 3', 'Ep 4', 'Ep 5', 'Ep 6']
#values = [watched_st['seen_ep1'].sum(), watched_st['seen_ep2'].sum(), watched_st['seen_ep3'].sum(), watched_st['seen_ep4'].sum(), watched_st['seen_ep5'].sum(), watched_st['seen_ep6'].sum()]
labels = ['Ep 1', 'Ep 2', 'Ep 3', 'Ep 4', 'Ep 5', 'Ep 6']
values = [watched_st['rank1'].mean(), watched_st['rank2'].mean(), watched_st['rank3'].mean(), watched_st['rank4'].mean(), watched_st['rank5'].mean(), watched_st['rank6'].mean()]

plt.bar(labels, values)

plt.title('Bar Graph of Ranking of each Star Wars movie \n (lower ranking, the better the movie)')
plt.xlabel('Star Wars movie')
plt.ylabel('Points')

plt.yticks([0,1,2,3,4,5])

plt.savefig('bargraph(watchedstartrek)_views_each_movie.png', dpi=100)

plt.show()

