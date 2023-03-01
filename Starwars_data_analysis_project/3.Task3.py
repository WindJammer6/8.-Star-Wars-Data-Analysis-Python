#Instructions
#1. Convert each column above so that it only contains the values True and False.
#2. Rename each of the columns above so the names are more intuitive. We recommend using seen_1 to indicate whether the respondent saw Star Wars: Episode I The Phantom Menace, seen_2 for Star Wars: Episode II Attack of the Clones, and so on.

import pandas as pd

#For some reason the '.fillna()' function to replace all NaN values to the string 'NaN' in the previous code always disappears
#when importing the csv file into another code, hence need to refill them again in this code again
starwars = pd.read_csv('StarWars2.csv', encoding="ISO-8859-1")
starwars['Have you seen any of the 6 films in the Star Wars franchise?'].fillna('NaN', inplace=True)
starwars['Do you consider yourself to be a fan of the Star Wars film franchise?'].fillna('NaN', inplace=True)

#Using '.replace()' function may work as well
#Along with using 'rename()' function to rename column names in a dataframe
#starwars = starwars.rename(columns = {'Which of the following Star Wars films have you seen? Please select all that apply.': 'seen_ep1', 'Unnamed: 4': 'seen_ep2', 'Unnamed: 5': 'seen_ep3', 'Unnamed: 6': 'seen_ep4', 'Unnamed: 7': 'seen_ep5', 'Unnamed: 8': 'seen_ep6'})

#'.isnull()' function detects missing values for an array-like object and returns True for null, and False if not
#null. Added '~' to reverse the Boolean markings
starwars2 = ~starwars.iloc[:,4:10].isnull().copy()
print(starwars2['Which of the following Star Wars films have you seen? Please select all that apply.'])

#Drop columns of index 4 to 9 
starwars = starwars.drop(columns=['Which of the following Star Wars films have you seen? Please select all that apply.' ,'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'])

#Inserting columns back (The only method that worked for me, tho definitely have better ways to do this)
starwars.insert(4, 'seen_ep1', starwars2['Which of the following Star Wars films have you seen? Please select all that apply.'])
starwars.insert(5, 'seen_ep2', starwars2['Unnamed: 4'])
starwars.insert(6, 'seen_ep3', starwars2['Unnamed: 5'])
starwars.insert(7, 'seen_ep4', starwars2['Unnamed: 6'])
starwars.insert(8, 'seen_ep5', starwars2['Unnamed: 7'])
starwars.insert(9, 'seen_ep6', starwars2['Unnamed: 8'])

#This line of code does not work for some reason (using what I have learnt from Pandaslearn folder:)
#starwars.loc[starwars['Which of the following Star Wars films have you seen? Please select all that apply.'] == 'Star Wars: Episode I  The Phantom Menace', 'Which of the following Star Wars films have you seen? Please select all that apply.'] = 'True'
#starwars = starwars.loc[starwars['Unnamed: 4'] == 'Star Wars: Episode II  Attack of the Clones', 'Unnamed: 4'] = 'True'
#starwars = starwars.loc[starwars['Unnamed: 5'] == 'Star Wars: Episode III Revenge of the Sith', 'Unnamed: 5'] = 'True'
#starwars = starwars.loc[starwars['Unnamed: 6'] == 'Star Wars: Episode IV A New Hope', 'Unnamed: 6'] = 'True'
#starwars = starwars.loc[starwars['Unnamed: 7'] == 'Star Wars: Episode V The Empire Strikes Back', 'Unnamed: 7'] = 'True'
#starwars = starwars.loc[starwars['Unnamed: 8'] == 'Star Wars: Episode VI Return of the Jedi', 'Unnamed: 8'] = 'True'
#'Star Wars: Episode I The Phantom Menace', 'Star Wars: Episode II Attack of the Clones', 'Star Wars: Episode III Revenge of the Sith', 'Star Wars: Episode IV A New Hope', 'Star Wars: Episode V The Empire Strikes Back', Star Wars: Episode VI Return of the Jedi'

starwars.to_csv('StarWars3.csv')