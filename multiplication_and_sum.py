# Exercise 1: Calculate the multiplication and sum of two numbers

num1 = input("Please enter the first number: ")

num2 = input('Please enter the second number: ')

first_number = int(num1);
second_number = int(num2);

def product( a, b):
  return a * b;


def add( a, b ):
  return a + b;
  
if( first_number * second_number > 1000 ):
  result = first_number + second_number
  add(first_number, second_number)
else:
  result = first_number * second_number;
  product(first_number, second_number)

print(result)


# creating a function to calculate both the product and the sum
