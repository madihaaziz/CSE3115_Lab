a=int(input())
b=int(input())
c=int(input())

if a==0 or b==0 or c==0:
  print("Number must be greater than 0")
elif a==b==c:
  print("Entered three numbers are Equal")
elif a!=b and b!=c and c!=a:
  print("Entered three numbers are different")
else:
  print("Neither all equal nor different")