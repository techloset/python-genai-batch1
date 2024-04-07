 ## Basic utility functions in Python
 - time: This module provides various time-related functions.
```
import time
current_time = time.time()
print("Current time:", current_time)
time.sleep(2)

```
- datetime: Functions for manipulating dates and times.
```
import datetime
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)
specific_date = datetime.datetime(2023, 12, 25)
print("Specific date:", specific_date)

current_datetime = datetime.now()
print(current_datetime)

date_string = "2022-01-01"
formatted_date = datetime.strptime(date_string, "%Y-%m-%d")
print(formatted_date)

from datetime import timedelta

one_day = timedelta(days=1)
tomorrow = datetime.now() + one_day
print(tomorrow)

from datetime import date

today = date.today()
print(today)

from datetime import time

current_time = time(hour=12, minute=30, second=45)
print(current_time)

duration = timedelta(days=1, hours=6)
total_seconds = duration.total_seconds()
print(total_seconds)

```

- random: This module is used for generating random numbers.
```
import random
random_number = random.randint(1, 10)
print("Random number:", random_number)
random.shuffle(my_list)
print("Shuffled list:", my_list)
```

- math: This module provides mathematical functions.

```
import math
square_root = math.sqrt(25)
print("Square root:", square_root)
factorial = math.factorial(5)
print("Factorial:", factorial)
```

- os: This module provides functions for interacting with the operating system.

```
import os
current_directory = os.getcwd()
print("Current directory:", current_directory)
files_in_directory = os.listdir(current_directory)
print("Files in directory:", files_in_directory)
```
- sys: This module provides access to some variables used or maintained by the Python interpreter.

```
import sys
python_version = sys.version
print("Python version:", python_version)
command_line_arguments = sys.argv
print("Command line arguments:", command_line_arguments)
```

- calendar: Functions for working with calendars.
```
import calendar
cal = calendar.month(2023, 2)
print("Calendar:")
print(cal)

```
- re: Functions for working with regular expressions.

```
import re
pattern = re.search(r'\bhello\b', 'hello world')
if pattern:
    print("Pattern found!")

```

- round numbers 
  ```
  round(3.14159, 2)
  ```