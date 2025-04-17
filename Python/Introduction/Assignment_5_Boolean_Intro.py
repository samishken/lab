#Questions for this assignment
# 1) Convert Inputs:  Prompt the user to enter their age and whether they have a valid driver’s license (Yes/No).

age_input = input("Enter your age: ")
license_input = input("Do you have a driver's license? (Yes/No): ")


# 2) Convert the age input to an integer and the license input to a Boolean value (assume "Yes" is True and "No" is False).
age = int(age_input)
has_license = license_input.strip().lower() == "yes"

# 3) Evaluate Conditions: If the user is at least 18 years old and has a valid driver’s license, print "You can drive."
# If the user is under 18, print "You are too young to drive."
# If the user is 18 or older but does not have a valid driver’s license, print "You cannot drive without a license."

if age < 18:
    print("You are too young to drive.")
elif not has_license:
    print("You cannot drive without a license.")
else:
    print("You can drive.")




# 4) Logical Operations:  Create a Boolean variable can_drive that is True if both conditions (age and license) are satisfied, and False otherwise. Print the value of can_drive.
can_drive = age >= 18 and has_license
print(can_drive)

# 5) Additional Logic: Ask the user if they want to drive today (Yes/No). Convert this input to a Boolean value.
# If they can_drive and want to drive today, print "Great! Have a safe drive!" Otherwise, print "Okay, maybe next time."

drive_today = input("Do you want to drive today? (Yes/No): ")
if can_drive and drive_today == "Yes":
    print("Great! have a safe drive!")
else:
    print("Okay, maybe next time")