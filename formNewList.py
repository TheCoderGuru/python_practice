# Exercise 10: Create a new list from a two list using the following condition


first_list = [ 10, 20, 25, 30, 35 ]
second_list = [ 40, 45, 60, 75, 90 ]

result_list = []

for x in first_list:
  if not x % 2 == 0:
    result_list.append(x)

for y in second_list:
  if y % 2 == 0:
    result_list.append(y)

print('result list: ', result_list)
