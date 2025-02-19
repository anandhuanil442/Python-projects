print("Welcome to Tip calculator")
Total_bill = float(input("What was the total bill ? $"))
Tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
Number_of_people = int(input("How many people to split the bill?"))
bill_per_person= (Total_bill * (Tip / 100) + Total_bill) / Number_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay:${final_amount}")