# I created this code from the formula in my class 8 science textbook

def ab_name():
    print(f"WELCOME {name1.capitalize()}{bg2.capitalize()}")

# Entering name
print("Hello")
name = input("Please Enter Your Full Name: \n")
# Giving two choices
print("Do you want us to call us your full name or you acronym?")
hi = input("For displaying acronym type 1, For displaying full name type 2: \n")
if hi == "2":
    print(f"Welcome {name.capitalize()}")
# Code for finding abbreviation
if hi == "1":
    name1 = (name[0])
    bg = (name.index(" "))
    if bg == 1:
        bg2 = (name[2])
        ab_name()
    if bg == 2:
        bg2 = (name[3])
        ab_name()
    if bg == 3:
        bg2 = (name[4])
        ab_name()
    if bg == 4:
        bg2 = (name[5])
        ab_name()
    if bg == 5:
        bg2 = (name[6])
        ab_name()
    if bg == 6:
        bg2 = (name[7])
        ab_name()
    if bg == 7:
        bg2 = (name[8])
        ab_name()
    if bg == 8:
        bg2 = (name[9])
        ab_name()
    if bg == 9:
        bg2 = (name[10])
        ab_name()
    if bg == 10:
        bg2 = (name[11])
        ab_name()
    if bg == 11:
        bg2 = (name[12])
        ab_name()
    if bg == 12:
        bg2 = (name[13])
        ab_name()

# Input for gender
gender = input("Please Enter Your Gender(male/female): \n")
# Input for age
age = input("Please Enter Your Age(8-18): \n")
# Input for height and giving two choices
print("Will you enter your height in feet or cm?")
ask = input("For centimeters type (cm), for feet type (ft): \n")
if ask == "cm":
    height = (input("Please Enter Your Height in cm: \n"))
if ask == "ft":
    height = (input("Enter your height in feet without a decimal point or space: \n"))
    a = int(height[0])
    b = int(height[1:3])
    height_in_ft = (a*12)+b
    height = int(height_in_ft)*2.54
    print("Your height in cm is: " + str(height))

# Conforming all the above data
if hi == "2":
    print(f"{name.capitalize()} Your gender is: {gender} ,your age is {age} and your height is {height}cm")
if hi == "1":
    print(f"{name1.capitalize()}{bg2.capitalize()} Your gender is: {gender} ,your age is {age} and your height is {str(height)}")
print("Are all the above information correct?")
answer = input("yes/no: \n")
if answer == "yes":
    print("Calculating your age")
else:
    print("Please start again")
#     creating a loop for no
# Proceeding with the calculations
if age == "8" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 72 * 100) + "cm")
if age == "9" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 75 * 100) + "cm")
if age == "10" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 78 * 100) + "cm")
if age == "11" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 81 * 100) + "cm")
if age == "12" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 84 * 100) + "cm")
if age == "13" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 88 * 100) + "cm")
if age == "14" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 92 * 100) + "cm")
if age == "15" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 95 * 100) + "cm")
if age == "16" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 98 * 100) + "cm")
if age == "17" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 99 * 100) + "cm")
if age == "18" and gender == "male":
    print("Your height at the end of your growth period will be " + str(int(height) / 100 * 100) + "cm")
if age == "8" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 77 * 100) + "cm")
if age == "9" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 81 * 100) + "cm")
if age == "10" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 84 * 100) + "cm")
if age == "11" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 88 * 100) + "cm")
if age == "12" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 91 * 100) + "cm")
if age == "13" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 95 * 100) + "cm")
if age == "14" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 98 * 100) + "cm")
if age == "15" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 99 * 100) + "cm")
if age == "16" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 99.5 * 100) + "cm")
if age == "17" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 100 * 100) + "cm")
if age == "18" and gender == "female":
    print("Your height at the end of your growth period will be " + str(int(height) / 100 * 100) + "cm")
# Printing thank you
if hi == "2":
    print("Thank you " + name + " for coming to this website")
if hi == "1":
    print(f"Thank you {name1.capitalize()}{bg2.capitalize()} for coming to this website")
