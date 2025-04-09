weight = int(input("enter your weight"))
height = int(input("enter your height"))
bmi = weight / (height ** 2)
if bmi <= 18.5:
    print(" you are underweight")
elif bmi <= 25:
    print("you are normal weight")
else:
    print("you are over weight")