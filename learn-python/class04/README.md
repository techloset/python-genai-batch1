# Class Topics
- Python - Functions
- Python Comments


## Python - Functions
**Types** of Python Functions
- Built-in functions
- Functions defined in built-in modules
- User-defined functions
keyword **def** followed by the function name and parentheses ( )
```
def greetings():
   print ("Hello World")

greetings()
```
  Types of Function Arguments
- Positional or required arguments
- Keyword arguments
- Default arguments
- Positional-only arguments
- Keyword-only arguments
- Arbitrary or variable-length arguments

```
def PrintMe( name, age = 35 ):
   print ("Name: ", name)
   print ("Age ", age)
# Positional or required arguments
PrintMe(10,20)

# Default arguments
PrintMe(10)

# Keyword-only arguments
def PrintMe(*, name, age = 35, num ):

make an argument positional-only, use the "/" symbol. All the arguments before this symbol will be treated as position-only.
def myfunction(x, /, y, *, z):
   print (x, y, z)
```


## Python Comments

Python supports two types of comments:
- Single-line comments
- Multi-line comments
### Single Line Comments 
Symbol # marks the beginning of comment line
```
# This is a comment
print ("Hello World")

```
If # is used in the middle of a line, text before it is a valid Python expression, while text following it is treated as comment

```
print ("How are you?") # This is also a comment but after a statement.
```

### Multi-line Comment in Python
A **triple quoted multi-line string** is also treated as comment if it is not a docstring of a function or class.

```
'''
First line in the comment
Second line in the comment
Third line in the comment
'''
print ("Hello World")
```
