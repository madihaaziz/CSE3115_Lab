n=int(input())
a=n
rev=0
while(a!=0):
  r=a%10
  rev=rev*10+r
  a=a//10
print(rev)
ab_diff=n-rev
d=ab_diff
print(ab_diff)

c=0
while d%2==0:
  c+=1
  d=d//2
  # j+=1
print(c) 
