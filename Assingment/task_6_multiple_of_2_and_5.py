                 #assingment-6
#Write the Python code of a program that reads an integer as input from the user, and prints the integer if it is a multiple of 2 and 5 and prints "Not a multiple of 2 OR 5" otherwise..

number=int(input("Enter the number : "))

if (number%2==0 and number%5 ==0 ):
    print("Multiple of 2 and 5 both",number )
elif (number%2==0) :
    print(number)
elif (number%5 ==0) :
    print(number)

else :
    print("Not a multiple of 2 OR 5")

# Sample Input 1:
# 5
# Sample Output 1:
# 5