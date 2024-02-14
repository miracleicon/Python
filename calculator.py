print("The Mayank Srivastav Calculator")

def add(m , n):
  return m + n

def subtract(m , n):
  return m - n

def multiplication(m , n):
  return m * n

def exponential(m , n):
  return m ** n

def divide(m , n):
  if n!=0:
     return m / n
  else: "Error! Cannot divide by zero"

def modulus(m , n):
  return m % n

def floordivision(m , n):
  return m // n

def calculator():
  print("Select operation.")
  print("1.Add")
  print("2.Subtraction")
  print("3.Multiplication")
  print("4.Exponential")
  print("5.Division")
  print("6.Modulus")
  print("7.Floor Division")

  choice = input("Enter choice(1/2/3/4/5/6/7): ")

  x = float(input("Enter First Number means value of m: "))
  y = float(input("Enter Second Number means value of n: "))

  if choice == '1':
    print("Addition of \"m\" and \"n\" is:", add(x,y))

  elif choice == '2':
    print("Subtraction of \"m\" and \"n\" is:", subtract(x,y))

  elif choice == '3':
    print("Multiplication of \"m\" and \"n\" is: " , multiplication(x,y))

  elif choice == '4':
    print("Exponential of \"m\" and \"n\" is: " , exponential(x,y))

  elif choice == '5':
    print("Division of \"m\" and \"n\" is:", divide(x,y))

  elif choice == '6':
    print("Modulus of \"m\" and \"n\" is:", modulus(x,y))

  elif choice == '7':
    print("Floordivision of \"m\" and \"n\" is:", floordivision(x,y))

  else:
    print("Wrong / Invalid input")

calculator()
