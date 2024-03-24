# Diccionario

informacion_personal = {
    'nombre':'Nthaly’,
    'edad':26,
    'ciudad’:’Shushufindi’,
    'provincia’:’Sucumbios’,
}
print('----------------------')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = 'Manabi'
informacion_personal['provincia'] = 'Portoviejo'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = ‘Ingeniera’

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0969848141'

# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('edad')

print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')