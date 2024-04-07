## Exception handling in Python
Exception handling in Python allows you to gracefully handle errors or exceptional situations that may occur during the execution of your code. This helps in writing robust programs that can recover from errors without crashing. Python provides a mechanism to catch and handle exceptions using the try, except, else, and finally blocks. Here's an overview of how exception handling works in Python:

- try: The try block is used to enclose the code that might raise an exception.

- except: The except block is used to handle the exception. If an exception occurs within the try block, Python looks for an appropriate except block that matches the type of exception raised.

- else: The else block is optional and is executed if no exception occurs in the try block.

- finally: The finally block is optional and is executed regardless of whether an exception occurs or not. It is often used for cleanup operations, such as closing files or releasing resources.

```
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero!")
else:
    # Executed if no exception occurs
    print("Division successful. Result:", result)
finally:
    # Cleanup or finalization code
    print("Cleanup operations here...")
```

You can also catch multiple exceptions or use a generic except block to catch any exception:

```
try:
    # Code that may raise an exception
    result = int(input("Enter a number: "))
except ValueError:
    # Handle ValueError
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    # Handle any other exception
    print("An error occurred:", e)

```

## File handling

File handling is a fundamental aspect of Python programming, allowing you to interact with files on your system. Here's an overview:

Key Concepts:

- open() function: This function is the gateway to file handling. It takes two arguments: filename and mode. The mode specifies how you want to interact with the file (read, write, append, etc.).

Modes: Common modes include:

r: Read (opens an existing file for reading)
w: Write (opens an existing file for writing, overwriting existing data)
x: Create (creates a new file, throws an error if the file exists)
a: Append (opens an existing file for appending data at the end)
r+, w+, a+: Combinations of read/write/append with the ability to move the file pointer
File object: When you call open(), it returns a file object, which you use to perform operations on the file. Common methods include:

- read(): Reads the entire file content as a string.
- readline(): Reads a single line from the file.
- readlines(): Reads all lines from the file and returns them as a list.
- write(data): Writes data to the file.
- close(): Closes the file (important to release resources).
- Context manager: The with statement is a convenient way to handle file opening and closing automatically, ensuring the file is closed even if exceptions occur.


```
file = open("example.txt", "r")  # Opens the file in read mode

# Read the entire content
content = file.read()

# Read a single line
line = file.readline()

# Read all lines into a list
lines = file.readlines()

file = open("example.txt", "w")  # Opens the file in write mode
file.write("Hello, World!\n")
file.write("This is a new line.\n")
file.close()

file = open("example.txt", "a")  # Opens the file in append mode
file.write("This is appended content.\n")
file.close()


with open("example.txt", "r") as file:
    content = file.read()
    print(content)



```


## Threads 
In Python, a thread refers to a sequence of instructions that can be executed independently within a process. Python provides a built-in module called threading which allows you to create and manage threads easily.

Here's a basic example of creating and starting a thread in Python:

```
import threading

# Define the function to be executed in parallel
def my_function(thread_num):
    print(f"Thread {thread_num} is running")

# Number of threads to create
num_threads = 5

# Create and start threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=my_function, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished")

```