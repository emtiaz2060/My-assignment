cgpa=float(input())
crd=int(input())

if crd>=30:  
    if 3.8>=cgpa>=3.89 :
      print("a=25")
    elif 3.90>=cgpa>=3.99:
      print("a=75")
    elif cgpa==4:
      print("a=100") 
    else:
        print("not eligible")
else:
    print("The student is not eligible for a waiver")






cgpas=float(input()) 
cred=int (input()) 

if cred>=30:

   if 3.8>=cgpa>=3.9:

     print("25 percent") 
    elif 3.90>=cgpa>=3.94: 
        print("50 percent") 
    elif 3.95>=cgpa>=3.99: 
        print("75 percent")

    elif cgpa==4: 
        print("100 percent") 
        else:
        print("not eligible")

else:

    print("The student is not eligible for a waiver")
    