print("welcome to python pizza")
size = input("What size do you want? S,M or L : ")
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("wrong input")

pepperoni = input("Do you want pepperoni on your pizza? y for yes and n for no ")
if pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill = bill + 3

extra_chees = input("do you want extra chees? y for yes and n for no ")
if extra_chees == "y":
   bill += 1
print(f"your final amount is ${bill}")
    
