print("Wecome to the tip calculator.")
bill=float(input("What was the total bill? $\n"))
tip=int(input("What percentage of tip you would like to give? 10, 12, 15 or more?\n"))
no_of_people=int(input("How many people to split up the bill?\n"))
# The bill amount percentage is stored in variable y
y= (bill*(tip/100))
# z is the bill amount to be payed each person
z= (bill+y)/no_of_people
# The rounded bill amount is stored in x
x= round(z,2)
print(f"Each person should pay: ${x}. Thank you.")