words = [
  'crab',
  'poison',
  'contagious',
  'simple',
  'bring',
  'sharp',
  'playground',
  'poison',
  'communion',
  'simple',
  'bring'
]

print(dict.fromkeys(words))

# Los diccionarios no pueden tener keys repetidas

new_list = list(dict.fromkeys(words))

print(words)
print(new_list)