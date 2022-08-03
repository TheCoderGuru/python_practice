# Exercise 1: Accept numbers from a user

first_num = input( 'Please enter the first number: ' )

second_num = input( 'Please enter the second number: ' )

a = int( first_num )
b = int( second_num )

def multiplyTwoNumbers( a, b ):
  
  return a * b;

print( 'The multiplication of %s and %s is %s' % ( a, b, multiplyTwoNumbers( a, b ) ) );
