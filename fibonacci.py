def fibonacci(num):
  if(num == 0):
    return 0
  elif(num == 1):
    return 1
  else:
    return fibonacci(num-1) + fibonacci(num-2)

num = input("Enter number to find fibonacci series: ")
print(fibonacci(int(num)))
