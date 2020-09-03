#User inputs  a series of numbers, when he inputs a negative number
#the program stops and outputs the largest positive number.
#We can use a for loop that repetedly asks the user for a number to
#input and then we add that to the max_int var, once we do that again
#we check if the number is positive, then we check if its larger than 
#max_int if it is we make it the new max_int


bool1 = True
max_int = int(0)
while bool1 == True:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int <= 0:
        bool1 = False
    if max_int <= num_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line
