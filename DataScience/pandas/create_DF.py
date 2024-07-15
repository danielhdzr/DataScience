import pandas as pd

column = ['Maria', 'Batman', 'Spongebob']
# Creo dict, y guardo los values de mi lista en el dict

titled_columns = {'name': column,
                'height': [1.67, 1.90, 0.25],
                'weight': [54, 100, 1]
                }

'''*******CREATE A DATAFRAME*******'''

'''Inserto mi dict into a data frame (table)
al imprimir lo vere en formato de tabla'''

data = pd.DataFrame(titled_columns)
'''
Sin formato tabla: 
{'name': ['Maria', 'Batman', 'Spongebob']}
  
En formato tabla:      
    name
0   Maria
1   Batman
2   Spongebob 
Cada key:value par es una columna. key = nombre, value = datos
'''
# Seleccionar una columna data[in the key of weight]
# select_column = data['weight']
# Seleccionar un value en especifico en columna especifica
# Acceder al peso de batman

'''*******SELECT VALUES FROM DATAFRAME*******'''
select_column = data['weight'][1]

'''
Seleccionar todos los values in the row of batman
[0]=maria, [1]=batman, [2]=spongebob
select_row = data.iloc[1]
'''

# Seleccionar solo el peso de batman
select_row = data.iloc[1]['weight']


'''*******MANIPULATE DATAFRAME VALUES*******'''
bmi = []
# weight/(height**2)
'''SLOW METHOD 
Se itera en la tabla o dataframe. Se recorre cada columna y cada row en esa columna.
[i] hace referencia al value almacenado en cada row de la columna especificada.
La operacion se realiza transversalmente, y da inicio en: 
el value[0] en height y el value[0] en weight. La iteracion continua a traves de los demas rows

for i in range(len(data)):
    bmi_score = data['weight'][i]/data['height'][i]**2
    # append a la lista bmi
    bmi.append(bmi_score)
# Creacion de nueva columna 'bmi
data['bmi'] = bmi
       
        name  height  weight        bmi
0      Maria    1.67      54  19.362473
1     Batman    1.90     100  27.700831
2  Spongebob    0.25       1  16.000000'''

'''FAST METHOD'''
# data es mi dataframe
# Creo una nueva comuna con el resultado de la operacion para cada row
data['bmi'] = data['weight']/data['height']**2

'''*******Save dataframe to a file*******'''
# data.to_csv('bmi.txt', sep='\t') # Guardado como txt
# index = False evita que se muestre la columan de index
data.to_csv('bmi.csv', index=False, sep='\t')

print(data)
