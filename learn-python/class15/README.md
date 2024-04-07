## The four pillars of Object-Oriented Programming (OOP) are:


- **Inheritance:** Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass). It promotes code reusability and establishes a hierarchy among classes.
  
```
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!
```

- **Encapsulation**: Encapsulation refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit (class). It hides the internal state of an object from the outside world and only exposes the necessary functionalities. This helps in maintaining data integrity and preventing unauthorized access.
```
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__speed = 0  # Encapsulation: speed is a private attribute

    def accelerate(self, increment):
        self.__speed += increment

    def get_speed(self):
        return self.__speed

my_car = Car("Toyota", "Camry")
my_car.accelerate(20)
print(my_car.get_speed())  # Output: 20
```

- **Abstraction:** Abstraction focuses on hiding the complex implementation details and showing only the essential features of an object to the outside world. It allows programmers to interact with objects without worrying about their internal complexities.

```
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 4)
print(rectangle.area())  # Output: 20

```



- **Polymorphism:** Polymorphism allows methods to do different things based on the object that calls them. In Python, polymorphism is achieved through method overriding and duck typing.

```
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!

```