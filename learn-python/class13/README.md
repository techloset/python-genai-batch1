# Class Topics
list of some commonly used string methods in Python:

Basic Operations:

**len(string)**: Returns the length of the string.
**str(object)**: Converts an object to a string.
Concatenation and Repetition:

**+** : Concatenates two strings.
*: Repeats a string a specified number of times.
Accessing Characters:

**string[index]**: Accesses a character at the specified index.
**string[start:end]**: Slices the string to extract a substring.
**string[start:end:step]**: Slices the string with a specified step.
String Case:

**string.lower()**: Converts all characters to lowercase.
**string.upper()**: Converts all characters to uppercase.
**string.capitalize()**: Capitalizes the first character.
**string.title()**: Converts the first character of each word to uppercase.
Whitespace Handling:

**string.strip()**: Removes leading and trailing whitespace.
**string.lstrip()**: Removes leading whitespace.
**string.rstrip()**: Removes trailing whitespace.
Search and Replace:

**string.find(substring)**: Returns the lowest index of the substring.
**string.index(substring)**: Returns the lowest index of the substring.
**string.count(substring)**: Returns the number of occurrences of the substring.
**string.replace(old, new)**: Replaces occurrences of the old substring with the new substring.
Checking Substrings:

**string.startswith(prefix)**: Checks if the string starts with a specific prefix.
**string.endswith(suffix)**: Checks if the string ends with a specific suffix.
**substring in string**: Checks if a substring is present in the string.
Character Information:

**string.isalpha()**: Returns True if all characters are alphabetic.
**string.isdigit()**: Returns True if all characters are digits.
**string.isalnum()**: Returns True if all characters are alphanumeric.
**string.isspace()**: Returns True if all characters are whitespace.
Formatting:

**string.format()**: Formats a string using placeholders.
**f-string**: Introduced in Python 3.6, allows embedding expressions inside string literals.
Encoding and Decoding:

**string.encode(encoding)**: Encodes the string into bytes.
**bytes.decode(encoding)**: Decodes bytes into a string.
