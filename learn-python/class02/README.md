# Class Topics

## Python Data Types
1. Numeric - **int**, **float**, **complex**
2. String - **str**
3. Boolean - **bool**
4. None - **NoneType**

## Built-in function type()
- type(123)
```
num1 = 123
result = type(123) 
print(result)
```

## Python Type Casting

- **Python Implicit** Casting
  language compiler/interpreter automatically converts object of one type into other, it is called automatic or implicit casting
  ``` 
  a=10   # int object 
  b=10.5 # float object
  ```

- **Python Explicit Casting**
Although automatic or implicit casting is limited to int to float conversion, you can use Python's built-in functions int(), float() and str() to perform the explicit conversions such as string to integer.
    ```
    a = int(10)
    a = float(9.99)
    a = str(10)
    ```