#Asks user for a input for what year
year = int(input("Enter a year: "))

#Checks the conditions if the year is divisible by 400
if year%400==0:
    print("It is a leap year")
    
#Checks the conditions if the year is divisible by 100 and 400
elif year%100==0 and year%400!=0:
    print("It is not a leap year")
    
#Checks the condition if the year is divisible by 4 and 100
elif year%4==0 and year%100!=0:
    print("It is a leap year")

else:
    print("It is not a leap year")
