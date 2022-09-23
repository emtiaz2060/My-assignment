              #task 9

#Write the Python code of a program that finds the number of hours, minutes, and seconds in a given number of seconds. The number of seconds is taken as input from the user

seconds = int(input("Enter a number(sec) : "))
minutes = seconds // 60
hours = minutes // 60
seconds -= (minutes*60)
minutes -= (hours*60)

print(f"{hours} hours {minutes} minutes {seconds} seconds")

# Sample Input 1:
# 10000
# Sample Output 1:
# Hours: 2 Minutes: 46 Seconds: 40