"""a=input()
b=input()
if a==b:
  print(f"{a} is same as {b}")
else:
  print("Both are not same")"""

a=int(input())
b=int(input())
if a>b:
  print(f"{a} is greater than {b}")
elif b>a:
  print(f"{b} is greater than {a}")
elif a==b:
  print(f"{b} is same as {a}")
else:
  print(f"{b} is different than {a}")