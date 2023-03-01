#Instructions:
#1. Convert each of the columns above to a float type.
#2. Give each column a more descriptive name. We suggest ranking_1, ranking_2, and so on.
import pandas as pd

starwars = pd.read_csv('StarWars3.csv', encoding="ISO-8859-1")
starwars['Have you seen any of the 6 films in the Star Wars franchise?'].fillna('NaN', inplace=True)
starwars['Do you consider yourself to be a fan of the Star Wars film franchise?'].fillna('NaN', inplace=True)

#Getting rid of 'Unnamed: 0' and 'Unnamed: 0.1' columns
starwars = starwars.set_index('RespondentID')
starwars = starwars.drop(columns='Unnamed: 0')
starwars = starwars.drop(columns='Unnamed: 0.1')
print(starwars.columns[8:14])

#Converting the datatypes to float for columns of index 8 to 14
starwars[starwars.columns[8:14]] = starwars[starwars.columns[8:14]].astype(float)

starwars = starwars.rename(columns={'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.':'rank1', 'Unnamed: 10':'rank2', 'Unnamed: 11':'rank3', 'Unnamed: 12':'rank4', 'Unnamed: 13':'rank5','Unnamed: 14':'rank6'})

starwars.to_csv('StarWars4.csv')