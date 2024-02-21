a=int(input())
b=int(input())
c=int(input())

if a<=b<=c:
  print("Increasing order")
elif a>=b>=c:
  print("Decreasing order")
else:
  print("Not in increasing or decreasing order")