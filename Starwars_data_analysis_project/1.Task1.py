#Instructions:
#. Read the dataset into a DataFrame.
#2. Explore the data by entering star_wars.head(10). Look for any strange values in the columns and rows.
#3. Review the column names with star_wars.columns.
import pandas as pd

#From the website instructions: We need to specify an encoding, because the dataset has some characters 
#that aren't in Python's default utf-8 encoding. You can read more about character encodings on developer 
#Joel Spolsky's blog. (this is still quite new to me. Ill leave this comment here to explain the 'encoding' function)
starwars = pd.read_csv('StarWars.csv', encoding="ISO-8859-1")
print(starwars.head(10))

print(starwars.columns)
