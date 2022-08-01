print( "Printing current and previous number and their sum in a range(10)" )

previous_num = 0

# loop from 1 to 10

for i in range( 1, 10 ):
  
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    
    # modify previous number
    
    # set it to the current number
    
    previous_num = i
