# Python

### Python functions
##### built-in functions
- print: writes text on the screen
- type: tells us the type of a certain value `print(type(a))`
- str: converts a number into a string
#####  define our own functions
- Define function `def`  
- Definition name of "greeting" -> `def greeting(name, department):`

##### Return values function (getting values out of a function)
- "return": tells the function to pass data back
- ou could also have a function return nothing, in which case the function simply exits.
- def area_triangel(base, height): return base*height/2

### Python Data Types
- Strings
- Integer (whole number without fractions)
- Float (Number with fractions)

### Python Variables
- Variables are names that we give to certain values in our programs.
    - length = 10 
    - width = 5
    - area = length * width
    - print(area)

###### Mixing two data types incorrectly
- print(7 + "8")
- "TypeError": unsupported operand type(s) for int and str

### Arithmetic operators
- Python can operate with numbers using the usual mathematical operators, and some special operators, too. These are all of them (we'll explore the last two in later videos).
- a + b = Adds a and b 
- a - b = Subtracts b from a 
- a * b = Multiplies a and b 
- a / b = Divides a by b 
- a ** b = Elevates a to the power of b. For non integer values of b, this becomes a root (i.e. a**(1/2) is the square root of a)
- a // b = (FLOOR DIVISION) The integer part of the integer division of a by b (no remainder)
- a % b = The remainder part of the integer division of a by b


### Expression
- A combination of numbers, symbols, or other values that produce a result when evaluated

### Explicit vs Implicit conversion
Some data types can be mixed and matched due to implicit conversion.
##### Implicit conversion:
- is where the interpreter helps us out and automatically converts one data type into another, without having to explicitly tell it to do so.
##### Explicit conversion:
- is where we manually convert from one data type to another by calling the relevant function for the data type we want to convert to. 
- We used when we wanted to print a number alongside some text. 
- We needed to call the str() function to convert the number into a string. 
- `print("The average size is: " + str(average))`


### Comparison (addition, subtraction, and division)
- Small than: <
- Greater than: >
- == Two things are equal to each other
- != not equal
##### logical operators (These logical operators are AND, OR and NOT)
- And: To evaluate as true the and operator would need both expressions to be true at the same time here.
- OR: the expression will be true if either of the expressions are true
- False: false only when both expressions are false



### Loops (While, For, Recursion)
##### While loops: 
- instruct your computer to continuously execute your code based on the value of a condition
- the body of the block can be executed multiple times instead of just once
- 
##### For loops
##### Recursion

