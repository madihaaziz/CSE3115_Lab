ul = int(input())
ll = int(input())
sum = 0
cn = 0
for i in range(ll, ul + 1, 1):
  # print(i)
  c = 0
  for j in range(1, i + 1):
    if i % j == 0:
      c += 1
  if c == 2:
    sum += i
    cn += 1
    print(i, end=" ")
print()
print("Sum of prime numbers: ", sum)
print("Number of prime numbers: ", cn)
