#Instructions:
#1. Convert the Have you seen any of the 6 films in the Star Wars franchise? column to the Boolean type.
#2. Convert the Do you consider yourself to be a fan of the Star Wars film franchise? column to the Boolean type.
#3. When you're finished, both columns should only contain the value True, False, or NaN.
#4. See number of yes, no and NaN for each column
import pandas as pd

starwars = pd.read_csv('StarWars.csv', encoding="ISO-8859-1")

a = starwars['Have you seen any of the 6 films in the Star Wars franchise?']
b = starwars['Do you consider yourself to be a fan of the Star Wars film franchise?']

starwars.loc[a == 'Yes', 'Have you seen any of the 6 films in the Star Wars franchise?'] = True
starwars.loc[a == 'No', 'Have you seen any of the 6 films in the Star Wars franchise?'] = False
starwars.loc[b == 'Yes', 'Do you consider yourself to be a fan of the Star Wars film franchise?'] = True
starwars.loc[b == 'No', 'Do you consider yourself to be a fan of the Star Wars film franchise?'] = False

#The 'fillna()' function (for datacleaning) replaces the NULL values with a specified value.
#The 'fillna()' function returns a new DataFrame object unless the inplace parameter is set to True, 
#in that case the fillna() method does the replacing in the original DataFrame instead.
a.fillna('NaN', inplace=True)
b.fillna('NaN', inplace=True)

#'value_counts()' function allows us to see all of the unique values in a column, 
#along with the total number of times each value appears.
#Started from row of index 1 to not get 'Response' as an unique value of the column
print(a.value_counts())
print(b.value_counts())

#Saved any changes to this temporary dataset cuz VS Code terminal dosen't let me see everything at once 
#whenever I want to print stuff for checking

starwars.to_csv('StarWars2.csv')