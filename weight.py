'''
This program asks the user to enter the weight of a package and then displays the shipping
charges and the total charges based on the weight and the rate per pound.
'''
print("Welcome to Damola Freight Shipping Incorporated! Enter your desired package weight to find our shipping charge estimates")

total_charges = 0

more = "y"

while more == "y":
    weight = int(input("Enter weight of package in pounds: "))
    charge = weight * rate_per_pound
    if weight < 2:
        rate_per_pound = 1.10
        print("Rate per pound: $1.10")
        print("The total charge is", charge)
    elif 2 <= weight < 6:
        rate_per_pound = 2.20
        print("Rate per pound: $2.20")
        print("The total charge is", charge)
    elif 6 <= weight < 10:
        rate_per_pound = 3.70
        print("Rate per pound: $3.70")
        print("The total charge is", charge)
    else:
        rate_per_pound = 3.80
        print("Rate per pound: $3.80")
        print("The total charge is", charge)
    charge = weight * rate_per_pound
    total_charges += charge

    more = input("Do you want to enter another weight <y/n>? ")
