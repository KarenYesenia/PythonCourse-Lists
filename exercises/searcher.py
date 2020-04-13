words = [
  'machine',
  'subset',
  'trouble',
  'starting',
  'matter',
  'eating',
  'truth',
  'disobedience'
]

input_word = input('Enter the word you want to search: ')

finded = False

for x in words:
  if x == input_word:
    print('We found the word!')
    print('The position is:', words.index(input_word))
    finded = True

if finded == False:
  print('Element not found')