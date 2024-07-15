import pandas as pd
import sqlite3 as sql3

# Lee archivo csv o txt
data = pd.read_csv('bmi.csv', sep='\t')
# Conecta a archivo sql
connection = sql3.connect('gta.db')

# Lee tabla SQL (no confundir tabla con archivo. En este caso comparten nombre)
gta_data = pd.read_sql('SELECT * FROM gta', connection)
# Print the table
print(gta_data)
# Print the first 5 rows
print(gta_data.head())
# Print the first 2 rows
print(gta_data.head(2))
# Print the last 2 rows
print(gta_data.tail(2))
'''
filtering command: gta_data[] 

Selected column ('city'): [ gta_data['city']

Value within the column: == 'Liberty City'] 

Full command: gta_data[ gta_data['city'] == 'Liberty City' ]  '''


'''*******FILTER AND REPLACE*******'''
filtered_row = gta_data[ gta_data['city'] == 'Liberty City' ] 
print(filtered_row)

replaced_city = gta_data.replace('Liberty City', 'New York')
print(replaced_city)

'''*******REMOVE DATA*******'''
# axis= 1 (columns)  axis=0 (rows)
removed_column = gta_data.drop('city', axis=1)
print(removed_column)
removed_column = gta_data.drop(['year','city'], axis=1)
print(removed_column) 
# Elimina los rows fuera del slice
removed_row = gta_data.iloc[1:4]
# Elimina los rows fuera del slice, y la columna 'city'
removed_row = gta_data.iloc[1:4].drop('city',axis=1)
print(removed_row) 

'''*******ADD NEW ROWS*******'''
row = {'year': '2021', 
       'name': 'Natural Vision Evolved', 
       'city': 'Los Angeles'
       }

new_row_data = gta_data._append(row, ignore_index=True)
print(new_row_data) 

### EXTRA ###
'''EVITA DUPLICADOS'''

jam_data = pd.read_csv('jamData.csv')
jam_data = jam_data.drop_duplicates( subset=['name / nickname (optional)'])
print('number of participants: ', len(jam_data))