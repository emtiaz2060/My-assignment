distance=int(input())
time=int(input())
distance=distance/1000
time=time/3600
velocity =distance/time
print("velocity",velocity)

if velocity<60 :
  print("Too slow.Needs more changes.")
elif 60<=velocity or velocity <=90:
  print("velocity is okey. the car is ready!")
elif velocity>90:
  print("too fast. only a few changes should suffice")
