#Question 1
# this code should rename all files with the extension .hpp to the extension .h.
# The function should then generate a new list called "newfilenames" that contains the file names with the new extension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
newfilenames = []
# using as many lines of code as your chosen method requires.
for filename in filenames:
  if ".hpp" in filename:
    newfilenames.append(filename.replace(".hpp", ".h"))
  else:
    newfilenames.append(filename)
print(newfilenames)

# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# 1) moving the first character to the end of each word;
# 2) then appending the letters "ay" to the end of each word.
def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        new_text = word[1:] + word[0] + "ay "
        say += new_text
        # Turn the list back into a phrase
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"



def guest_list(guests):
	for guest in guests:
		name, age, profession = guest
		print("{} is {} years old and works as {}".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])