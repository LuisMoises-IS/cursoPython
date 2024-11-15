set_contries = {'col', 'mex', 'bol'}

size = len(set_contries)
print(size)

# Buscar un elemento dentro del conjunto
print('col' in set_contries)
print('pe' in set_contries)

# Add
set_contries.add('pe')
print(set_contries)

# Update
set_contries.update({'ar', 'ecua', 'pe'})
print(set_contries)

# Remove
set_contries.remove('col')
print(set_contries)
set_contries.clear()
print(set_contries)

