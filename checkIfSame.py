# Exercise 5: Check if the first and last number of a list is the same

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def checkArray( array ):
  if( array[0] == array[-1]):
    return True;
  else:
    return False;

print('Given list ', numbers_x, '\n', 'result is ', checkArray(numbers_x))

print('numbers_y = ', numbers_y, '\n', 'result is ', checkArray(numbers_y))
