height = float(input("Please enter your height in inches: "))
weight = float(input("Dont be modest, enter your weight: "))
height_convert = height / 39.37
weight_convert = weight / 2.2
bodyweight_index = weight_convert / (height_convert**2)
print("Your BMI is: " + str(bodyweight_index))
