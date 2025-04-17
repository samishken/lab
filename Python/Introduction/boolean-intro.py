# Boolean Data Types
# It is commonly used for evaluating conditions

is_raining = True
is_sunny = False

print(is_raining) #output Ture
print(is_sunny) #Output False

is_server_up = True

if is_server_up:
    print("Server is up")
else:
    print("Server is down")

# Ask the user if the server is up or down
print("Is the server up or down?")
print("Enter 1 if the server is UP (True)")
print("Enter 2 if the server is DOWN (False)")

# Get user input
user_input = input("Your choice: ")

# Check the input and respond accordingly
if user_input == "1":
    print("The server is UP.")
elif user_input == "2":
    print("The server is DOWN.")
else:
    print("Invalid input. Please enter 1 or 2.")


