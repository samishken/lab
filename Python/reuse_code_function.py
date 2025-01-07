### make code reusable
### cleaning duplicated code
name= "Eric"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is: " + str(number))

name= "Cameron"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is: " + str(number))

### cleanup the above code
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is: " + str(number))
lucky_number("Eric")
lucky_number("Cameron")

