grade = float(input("Enter your grade:"))
if grade < 0 or grade > 20 :
     print("invalid grade")
elif grade >= 16:
   print("Excellent")
elif grade >= 14:
   print("Good")
elif grade >= 10:
   print("Average")
else :
   print("fail") 
