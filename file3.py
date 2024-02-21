a=int(input())
charge=0
if a<=50:
  charge=a*2
elif 50<a<=150:
  charge=100+(a-50)*3
elif a>150:
  charge=100+300+(a-150)*8
charge=charge+charge*0.2
print(charge)