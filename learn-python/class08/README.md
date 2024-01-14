# Class Topics

## Python - Lists
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

### Python List Operations
Python Expression	
Concatenation
[1, 2, 3] + [4, 5, 6]	  [1, 2, 3, 4, 5, 6]	
Repetition
['Hi!'] * 4	  ['Hi!', 'Hi!', 'Hi!', 'Hi!']
Membership
3 in [1, 2, 3]	True
1. Creating Lists:
You can create a list by enclosing a comma-separated sequence of items within square brackets []. For example:

my_list = [1, 2, 3, 'four', 5.0]
2. Accessing Elements:
Indexing: Lists are zero-indexed, meaning the first element has an index of 0. You can access elements using positive or negative indexing.

first_element = my_list[0]   # Accessing the first element
last_element = my_list[-1]   # Accessing the last element
Slicing: You can extract a sublist by specifying a range of indices.

sublist = my_list[1:4]   # Extract elements at index 1, 2, and 3
3. List Methods:
append(): Adds an element to the end of the list.

my_list.append(6)
extend(): Appends the elements of another iterable to the end of the list.

another_list = [7, 8, 9]
my_list.extend(another_list)
insert(): Inserts an element at a specified position.

my_list.insert(2, 'inserted')
remove(): Removes the first occurrence of a specified value.

my_list.remove(3)
pop(): Removes and returns an element at a specified index (or the last element if no index is specified).

popped_element = my_list.pop(4)
index(): Returns the index of the first occurrence of a specified value.

index_of_four = my_list.index('four')
count(): Returns the number of occurrences of a specified value.

count_of_2 = my_list.count(2)
sort(): Sorts the elements of the list in ascending order.

my_list.sort()
reverse(): Reverses the order of the elements in the list.

my_list.reverse()
clear(): Removes all elements from the list.

my_list.clear()

1. List Concatenation:
You can concatenate lists using the + operator.

concatenated_list = my_list + another_list
1. List Copying:
Be cautious when copying lists, as simple assignment (new_list = old_list) creates a reference, not a new copy. To create a copy, you can use the copy() method or the built-in list() constructor.

copied_list = my_list.copy()
1. List Length:
The len() function returns the number of elements in a list.

length_of_list = len(my_list)
1. List Membership:
You can check if an element is present in a list using the in keyword.

is_present = 3 in my_list

1.  List as Stack or Queue:
You can use lists as a basic stack (Last In, First Out) or queue (First In, First Out).

Stack
my_list.append(10)      # Push
popped_item = my_list.pop()  # Pop

Queue
my_list.append(10)      # Enqueue
dequeued_item = my_list.pop(0)  # Dequeue
11. Nested Lists:
Lists can contain other lists, creating nested structures.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


