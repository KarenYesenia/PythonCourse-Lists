# def get_Max(number_list):
#   if number_list[0] == number_list[1]:
#     print('Same numbers')
#   else:  
#     max_value = max(number_list)
#     print('The max value is:', max_value)

# def max_Number():
#   print('Lets check which number is bigger')
#   num_1 = float(input('First number: '))
#   num_2 = float(input('Second number: '))

#   num_list = []
#   num_list.append(num_1)
#   num_list.append(num_2)

#   get_Max(num_list)

# max_Number()

num_1 = float(input('First Number: '))
num_2 = float(input('Second Number: '))

if num_1 == num_2:
  print('Same value')
else:
  num_max = max(num_1, num_2)
  print(num_max)