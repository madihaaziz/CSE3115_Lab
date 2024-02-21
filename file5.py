gender=input()
score=int(input())
region=input()

if gender=="Male":
  if score>=60 and (region=="Bengaluru" or       
     region=="bengaluru"):
      print("Eligible")
  else:
      print("Not Elgible")
else:
  print("Not Elgiible")