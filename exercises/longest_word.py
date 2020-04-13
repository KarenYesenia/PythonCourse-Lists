
# def longest_word():
  

# longest_word()

print('Lets see which word is the longest')
print('Heres the list')
words = [
  'mystery',
  'brother',
  'aviator',
  'crocodile',
  'pearl',
  'orchard',
  'crackpot'
]
print(words)
longest = max(words, key=len)
print('The longest word is:', longest)