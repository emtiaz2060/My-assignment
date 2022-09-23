                                     #assingment-8
 #Write the Python code of a program that reads an integer, and prints the integer if it is a multiple of 2 AND 5 and prints "Not multiple of 2 and 5 both" otherwise.            


number=int(input("Enter the number : "))

if (number%2==0 and number%5 ==0 ):
    print(number )
else:
    print("Not multiple of 2 and 5 both")

# #Sample Input 2:
# 15
# Sample Output 2:
# Not multiple of 2 and 5 both