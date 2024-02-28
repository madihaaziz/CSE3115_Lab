
# i=0
# while i<6:
#   i+=1
#   if i==3:
#     continue
#   print(i)

# i=1
# while i<6:
#   print(i)
#   if i==3:
#     break
#   i+=1

# for i in range(1,11,1):
#   print(i)
# for i in range(0,11,2):
#   print(i)

a=int(input())
c=0
for i in range(1,a+1):
  if a%i==0:
    c+=1
  else:
    continue
if c==2:
  print("Prime")
else:
  print("composite")