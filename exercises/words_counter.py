words = [
  'machine',
  'matter',
  'subset',
  'trouble',
  'starting',
  'matter',
  'eating',
  'matter',
  'truth',
  'disobedience',
  'matter',
  'truth'
]

count = 0
found = False

input_word = input('Which word you wanna search? ')

for x in words:
  if x == input_word:
    count += 1
    found = True

print('Word', input_word, '- Count:', count)












# matches = [x for x in words if x == input_word]
# print(matches)