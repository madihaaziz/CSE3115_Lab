a = int(input())
n = a
num = 0
while n > 0:
  i = n % 10
  num = num * 10 + i
  n = n // 10
if num == a:
  print("Palindrome")
else:
  print("Not a palindrome")
