gender = input()
if gender == "Male":
  score = int(input())
  region = input()
  if score >= 60 and (region == "Bengaluru" or region == "bengaluru"):
    print("Eligible")
  else:
    print("Not Elgible")
else:
  print("Not Elgiible")
