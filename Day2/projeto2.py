print("Welcome to the tip calculator")
bill = float(input("What was the total bill? R$"))
tip = int(input("What porcentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

new = bill  + (bill *(tip)/100)
result = new / people
print(f"Each person should pay R${round(result, 2)}")