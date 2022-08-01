# Exercise 3: Print characters from a string that are present at an even index number

str = input( 'Please enter a string: ' )

print( str )

x = 0

for x in range(0, len(str) - 1, 2):

  if( x % 2 == 0 ):
    
    print( str[ x ] )
