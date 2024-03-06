id=int(input())
num=id;
sum=0;
while(num!=0):
  rem=num%10;
  sum+=rem;
  num=num//10;
  if(sum>26):
    num=sum
    sum=0
print(sum)
print(chr(64+sum))



    