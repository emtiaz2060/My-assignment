                      #assingment-6
#Write the Python code of a program that reads an integer, and prints the integer it is a multiple of either 2 or 5 but not both. If the number is a multiple of 2 and 5 both, then print "Multiple of 2 and 5 both". For all other numbers, the program prints "Not a multiple we want".
number=int(input("Enter the number : "))

if( number %2==0 ) :
    print(number)
elif( number %5 ==0 ) :
    print(number)
else:
    print ("Not a multiple we want")
      
# Sample Input :
# 10
# Sample Output :
# Multiple of 2 and 5 both

