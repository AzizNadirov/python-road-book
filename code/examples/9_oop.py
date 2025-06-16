# Object Oriented Programming (OOP)

## without OOP is hard
def take_person(name: str, surname: str, birth_year: int)->dict:
    """ take users properties """
    return {"name": name,
            "surname": surname,
            "birth_year": birth_year}

def get_age(person: dict)->int:
    """ calculate age of person """
    current_year = 2024
    return current_year - person.get("birth_year")

veli = take_person(name="Vəli", 
                   surname="Vəliyev",
                   birth_year=1990)

eli = take_person(name="Əli", 
                   surname="Vəliyev",
                   birth_year=1993)

print(f"Vəlinin yaşı: {get_age(veli)}; Əlinin yaşı: {get_age(eli)}")


## with OOP
class Person:
    name = "boş"
    surname = "boş"

p1 = Person()
print("p1.name: ", p1.name)
print("p1.surname: ", p1.surname)



class Person:
    name = "boş"
    surname = "boş"

p1 = Person()
print("p1.name: ", p1.name)
print("p1.surname: ", p1.surname)

print("--------------------------")
p1.name = "Əli"
p1.surname = "Vəliyev"
p1.email = "ali.valiyev@fakemail.com"

print("p1.name: ", p1.name)
print("p1.surname: ", p1.surname)
print("p1.email: ", p1.email)

# p1.name:  boş
# p1.surname:  boş
# --------------------------
# p1.name:  Əli
# p1.surname:  Vəliyev
# p1.email:  ali.valiyev@fakemail.com


## constructor
class Person:
    def __init__(self, name: str, surname: str):
        print("in __init__")
        self.ad = name
        self.soyad = surname
        print("__init__ done.")
    
p1 = Person(name="Əli", surname="Vəliyev")
print(f"Ad: {p1.ad}; Soyad: {p1.soyad}")
print(p1.name)      # biz 'name' adlı xüsusiyyət yaratmamışıq

# in __init__
# __init__ done.
# Ad: Əli; Soyad: Vəliyev
# AttributeError: 'Person' object has no attribute 'name'



## with methods
class Person:
    def __init__(self, name: str, surname: str, birth_year: str):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def get_age(self)->int:
        current_year: int = 2024
        return current_year - self.birth_year
    
p1 = Person(name="Əli", surname="Vəliyev", birth_year=1995)
print(f"Ad: {p1.name}; Soyad: {p1.surname}")
p1_age = p1.get_age()
print(f"Doğum ili: {p1.birth_year} Yaşı: {p1_age}")

# Ad: Əli; Soyad: Vəliyev
# Doğum ili: 1995 Yaşı: 29




class Person:
    def __init__(self, name: str, surname: str, birth_year: str):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def get_age(self)->int:
        current_year: int = 2024
        return current_year - self.birth_year
    
    def generate_email(self, domain: str)->str:
        replacements = {'ə': 'e', 'ğ': 'gh', 'ç': 'ch', 'ı': 'i', 'ü': 'u'}
        email = f"{self.name}.{self.surname}@{domain}".lower()
        for letter in replacements.keys():
            email = email.replace(letter, replacements[letter])
        return email
    
p1 = Person(name="Əli", surname="Vəliyev", birth_year=1995)
print(f"Ad: {p1.name}; Soyad: {p1.surname}")
p1_age = p1.get_age()
print(f"Doğum ili: {p1.birth_year} Yaşı: {p1_age}")
email = p1.generate_email("fakemail.com")
print(f"Email: {email}")



# Ad: Əli; Soyad: Vəliyev
# Doğum ili: 1995 Yaşı: 29
# Email: eli.veliyev@fakemail.com




class Person:
    def __init__(self, id: int, name: str, surname: str, birth_year: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def get_age(self)->int:
        current_year: int = 2024
        return current_year - self.birth_year
    
    def generate_email(self, domain: str)->str:
        replacements = {'ə': 'e', 'ğ': 'gh', 'ç': 'ch', 'ı': 'i', 'ü': 'u'}
        email = f"{self.name}.{self.surname}@{domain}".lower()
        for letter in replacements.keys():
            email = email.replace(letter, replacements[letter])
        return email
    
p1 = Person(0, "Ali", "Valiyev", 1990)
p2 = Person(1, "Hikmet", "Nesibov", 2000)
p3 = Person(2, "Arzu", "Salmanli", 1999)



## class variables and methods
class Triangle:
    sides: int = 3
    def __init__(self, d1: float, d2: float, d3: float):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    
    def get_perimeter(self)->float:
        return self.d1 + self.d2 + self.d3

t1 = Triangle(5, 5, 7)
t2 = Triangle(10, 5, 11.1)

print("t1 Figure sides: ", t1.sides)
print("t2 Figure sides: ", t2.sides)

print("t1 Perimeter: ", t1.get_perimeter())
print("t2 Perimeter: ", t2.get_perimeter())

# t1 Figure sides:  3
# t2 Figure sides:  3
# t1 Perimeter:  17
# t2 Perimeter:  26.1



class Car:
    wheels = 4
    doors = 4
    def __init__(self, brand: str, model: str)->None:
        self.brand = brand
        self.model = model

    @classmethod
    def class_info(cls)->str:
        return f"Cars with {cls.wheels} wheels and {cls.doors} doors."
    
m5 = Car(brand='BMW', model='M5')
print("m5.brand, m5.model, m5.wheels, m5.doors:")
print('\t', m5.brand, m5.model, m5.wheels, m5.doors)
print("class info:")
print('\t', Car.class_info())

# m5.brand, m5.model, m5.wheels, m5.doors:
# 	 BMW M5 4 4
# class info:
# 	 Cars with 4 wheels and 4 doors.



class Email:
    domain = "@fakemail.com"
    separator = "."
    def __init__(self, name: str, surname: str)->None:
        self.name = name
        self.surname = surname
        self.email = self.build_email(name=self.name, surname=self.surname)
    
    @classmethod
    def build_email(cls, name: str, surname: str)->str:
        replacements = {'ə': 'e', 'ğ': 'gh', 'ç': 'ch', 'ı': 'i', 'ü': 'u'}
        email = f"{name}{cls.separator}{surname}{cls.domain}".lower()
        for letter in replacements.keys():
            email = email.replace(letter, replacements[letter])
        return email
    
    @classmethod
    def from_string(cls, string: str, separator=' ')->str:
        name, surname = string.split(separator)[:2]
        email = cls.build_email(name=name, surname=surname)
        return email
    
e1 = Email("Əli", "Vəliyev")
print(e1.email)     # eli.veliyev@fakemail.com
print(Email.from_string("Hikmət Nəsibov"))  # hikmet.nesibov@fakemail.com





class Triangle:
    sides = 3
    def __init__(self, d1: float, d2: float, d3: float):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

@staticmethod
def calc_perimeter(d1: float, d2: float, d3: float):
    return sum([d1, d2, d3])

def get_perimeter(self):
    return self.d1 + self.d2 + self.d3

t1 = Triangle(5, 5, 7)
print(t1.calc_perimeter(5, 5, 7))   # nüsxə üzərindən #17
print(Triangle.calc_perimeter(5, 5, 7)) # sinif üzərindən #17



## property:
class Triangle:
   sides = 3
   def __init__(self, d1: float, d2: float, d3: float):
       self.d1 = d1
       self.d2 = d2
       self.d3 = d3
       self.__p = self.d1 + self.d2 + self.d3
       
   @property    
   def perimeter(self):
       print("Getting Perimeter...")
       return self.__p
    
t = Triangle(1,2,3)
print(f"t.perimeter: {t.perimeter}")
# Getting Perimeter...
# t.perimeter: 6



class Triangle:
    sides = 3
    def __init__(self, d1: float, d2: float, d3: float):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.__p = self.d1 + self.d2 + self.d3
        
    @property    
    def perimeter(self):
        print("Getting Perimeter...")
        return self.__p
    
    @perimeter.setter
    def perimeter(self, value):
        if self.__p != value:
            print("You are setting incorrect value...")
        else:
            self.__p = value
        
t = Triangle(1,2,3)
print(f"t.perimeter: {t.perimeter}")
t.perimeter = -1
print(f"t.perimeter: {t.perimeter}")
t.perimeter = 6.0
print(f"t.perimeter: {t.perimeter}")

# Getting Perimeter...
# t.perimeter: 6
# You are setting incorrect value...
# Getting Perimeter...
# t.perimeter: 6
# Getting Perimeter...
# t.perimeter: 6.0


### Person + file
from typing import List
   
class Person:
    def __init__(self, id, name, surname, birth_year):
        self.id = id
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def get_age(self):
        current_year = 2024
        return current_year - self.birth_year
    
    def generate_email(self, domain):
        replacements = {'ə': 'e', 'ğ': 'gh', 'ç': 'ch', 'ı': 'i', 'ü': 'u'}
        email = f"{self.name}.{self.surname}@{domain}".lower()
        for letter in replacements.keys():
            email = email.replace(letter, replacements[letter])
        return email
    
    @staticmethod
    def person_to_str(person: 'Person', sep: str)->str:
        return f"{person.id}{sep}{person.name}{sep}\
            {person.surname}{sep}{person.birth_year}\n"
    
    @classmethod
    def str_to_person(cls, person_str: str, sep: str)->'Person':
        splitted_person = person_str.split(sep)
        id_, name, surname, birth_year = splitted_person
        person_instance = cls(id_, name, surname, birth_year)
        return person_instance

    @classmethod
    def upload(cls, 
                people: List['Person'], 
                to: str, 
                overwrite: bool=False, 
                sep=',')->None:
        """ upload people as text into file """
        print(f"Uploading people into '{to}', overwrite: '{overwrite}' ")
        mode = 'w' if overwrite else 'a'
        with open(to, mode) as file:
            for person in people:
                person_str = cls.person_to_str(person, sep=sep)
                file.write(person_str)
        print("Done.")

    @classmethod
    def load(cls, file_path: str, sep=',')->List['Person']:
        """ load list of Person instances from file """
        people = []
        with open(file_path, 'r') as file:
            file_lines = file.readlines()
            for person_str in file_lines:
                person_instance = cls.str_to_person(person_str=person_str, 
                                                    sep=sep)
                people.append(person_instance)
        return people

# 1. Nüsxələri yaradaq
p1 = Person(0, "Ali", "Valiyev", 1990)
p2 = Person(1, "Hikmet", "Nesibov", 2000)
p3 = Person(2, "Arzu", "Salmanli", 1999)

# 2. people.txt faylına yazaq
filename = 'people.txt'
person_list = [p1, p2, p3]
Person.upload(people=person_list, to=filename, overwrite=True)

# 3. Fayldan yükləyək
loaded_people = Person.load(file_path=filename)
print("Loaded People: ", loaded_people)

# Uploading people into 'people.txt', overwrite: 'True' 
# Done.
# Loaded People:  
#     [<__main__.Person object at ...>, 
#     <__main__.Person object at ...>, 
#     <__main__.Person object at ...>]
   




## Inheritance
class Student(Person):
    def __init__(self,
                 id: int,
                 name: str, 
                 surname: str,
                 birth_year: int,
                 university: str,
                 group: str,
                 entry_year: int,
                 entry_point: int
                 ):
        super().__init__(id, name, surname, birth_year)
        self.university = university
        self.group = group
        self.entry_year = entry_year
        self.entry_point = entry_point

    def get_course(self)->int:
        current_year = 2024
        return current_year - self.entry_year
    
veli = Student(id=0, name="Veli", surname="Veliyev", birth_year=2005, university="BDU", 
               group="1234A", entry_year=2022, entry_point=450)

print("veli.name: ", veli.name)
print("veli.university: ", veli.university)
print("veli.get_age(): ", veli.get_age())
print("veli.get_cource: ", veli.get_course())
print("veli.generate_email: ", veli.generate_email(domain="fakemail.com"))

# veli.name:  Veli
# veli.university:  BDU
# veli.get_age():  19
# veli.get_cource:  2
# veli.generate_email:  veli.veliyev@fakemail.com



class A:
    a = "A.a"
    b = "A.b"
    def method(self):
        print("method, from class: ", self.__class__.__name__)

class B(A):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def method(self):
        print("method, from class: ", self.__class__.__name__)

b1 = B("B")
print(f"b1.b: {b1.b}")
print(f"b1.a: {b1.a}")

# b1.b: A.b
# b1.a: B




## Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

    def start(self):
        return "Vehicle is starting..."

    def stop(self):
        return "Vehicle is stopping..."

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, {self.num_doors} doors"

    def drive(self):
        print(self.start())
        print("Car is driving...")
        print(self.stop())

class Boat(Vehicle):
    def __init__(self, make, model, year, length):
        super().__init__(make, model, year)
        self.length = length

    def display_info(self):
        return f"{super().display_info()}, {self.length} feet long"

    def float(self):
        print(self.start())
        print("Boat is floating...")
        print(self.stop())

class Plane(Vehicle):
    def __init__(self, make, model, year, max_altitude):
        super().__init__(make, model, year)
        self.max_altitude = max_altitude

    def display_info(self):
        return f"{super().display_info()}, {self.max_altitude} max altitude"

    def fly(self):
        print(self.start())
        print("Plane is flying...")
        print(self.stop())
        
x5 = Car("BMW", "X5", 2022, num_doors = 4)
boing = Plane("Boing", "747", 2020, max_altitude = 100)
searay = Boat("Searay", "SunDancer", 2021, length = 20)
print('--------------------------------------')
print(x5.drive()) 
print('--------------------------------------')
print(boing.fly())
print('--------------------------------------')
print(searay.float())
print('--------------------------------------')

# --------------------------------------
# Vehicle is starting...
# Car is driving...
# Vehicle is stopping...
# None
# --------------------------------------
# Vehicle is starting...
# Plane is flying...
# Vehicle is stopping...
# None
# --------------------------------------
# Vehicle is starting...
# Boat is floating...
# Vehicle is stopping...
# None
# --------------------------------------





### Scaler example
from numbers import Number
   
class MathStructure:
   shape = None
   def add(self, other):
       pass

   def sub(self, other):
       pass

   def validate(self):
       pass


class Scalar(MathStructure):
   shape = 0
   def __init__(self, value: Number) -> None:
       self.value = value
       self.validate()

   def validate(self):
       """ raise error if value is not a number """
       if not isinstance(self.value, Number):
           raise TypeError(f"Scalar value must be numeric, not {type(self.value)}")

   def add(self, other):
       if isinstance(other, Scalar):
           return Scalar(self.value + other.value)
       elif isinstance(other, Number):
           return Scalar(self.value + other)
       else:
           return None

   def sub(self, other):
           if isinstance(other, Scalar):
               return Scalar(self.value - other.value)
           elif isinstance(other, Number):
               return Scalar(self.value - other)
           else:
               return None
   
s1 = Scalar(1)
s2 = Scalar(2.0)
s3 = s1.add(s2)
s4 = s3.sub(10)
print(s3.value, s4.value)   # 3.0 -7.0
print(s3.shape, s4.shape)   # 0 0





## Vector

class Vector(MathStructure):
    shape = (None, )
    def __init__(self, values: list) -> None:
        self.values = values
        self.validate()
        self.shape = (len(self.values),)
        self.values = self.as_tuple()

    def as_tuple(self)->tuple:
        return tuple(self.values)

    def validate(self):
        """ raise error if values is not list """
        # 1. validate `values`
        if not isinstance(self.values, (list, tuple)):
            raise TypeError(f"Vector values must be list or tuple, not {type(self.values)}")
        # 2. validate items in `values`
        if len(self.values) > 0:
            first_type = type(self.values[0])
            for item in self.values:
                if not isinstance(item, first_type):
                    raise TypeError(f"Vector values must be all same type.")

    def add(self, other):
       if isinstance(other, Vector):
           if self.shape == other.shape:
               return Vector([x + y for x, y in zip(self.values, other.values)])
           else:
               return None
       elif isinstance(other, Number):
           return Vector([x + other for x in self.values])
       
       elif isinstance(other, Scalar):
           return Vector([x + other.value for x in self.values])
       else:
           return None
               
   def sub(self, other):
       if isinstance(other, Vector):
           if self.shape == other.shape:
               return Vector([x - y for x, y in zip(self.values, other.values)])
           else:
               return None
           
       elif isinstance(other, Scalar):
           return Vector([x - other.value for x in self.values])
       
       elif isinstance(other, Number):
           return Vector([x - other for x in self.values])
       else:
           return None
            
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = v1.add(v2)
v4 = v1.sub(1)

print(f"v1.add(v2): {v3.values}")
print(f"v1.sub(1):  {v4.values}")

# v1.add(v2): (5, 7, 9)
# v1.sub(1):  (0, 1, 2)
# v1.shape: (3,)
# v2.shape: (3,)




## Vector V2:
class Vector(MathStructure):
    shape = (None, )
    def __init__(self, values: list) -> None:
        self.values = values
        self.validate()
        self.length = self._get_len()
        self.shape = (self.length,)
        self.values = self.as_tuple()
    
    def _get_len(self) -> int:
        return len(self.values)
    
    def _get_mean(self) -> float:
        return round(sum(self.values) / self.length, 3)
    
    def _get_min(self)->Number:
        return min(self.values)
        
    def _get_max(self) -> Number:
        return max(self.values)
    
    def _get_range(self) -> Number:
        return max(self.values) - min(self.values)
    
    def get_stat(self) -> dict:
        """ calculate basic statistics """
        mean = self._get_mean()
        min_ = self._get_min()
        max_ = self._get_max()
        range_ = self._get_range()
        return {'mean': mean, 'min': min_, 
                'max': max_, 'range': range_}
        
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = v1.add(v2)
v4 = v1.sub(1)

print(f"v1.add(v2): {v3.values}")
print(f"v1.sub(1):  {v4.values}")
print(f"v2.get_stat(): {v2.get_stat()}")

# v1.add(v2): (5, 7, 9)
# v1.sub(1):  (0, 1, 2)
# v2.get_stat(): {'mean': 5.0, 'min': 4, 'max': 6, 'range': 2}




## Special Methods
from numbers import Number
from typing import Union, Self
   
class Num:
   def __init__(self, value: Number):
       self.__value = value
       
   def __add__(self, other: Union[Self, Number]):
       if isinstance(other, Number):
           sum_ = other + self.__value
       elif isinstance(other, Num):
           sum_ = self.__value + other.__value
       else:
           raise ValueError(f"Unsupported + for {type(self)} and {type(other)}")
       return Num(value=sum_)
   
   def __str__(self):
       return f"Number: {self.__value}"
   
num_1 = Num(value=1)
num_2 = Num(value=2)
num_3 = num_1 + num_2   # 3
num_4 = num_3 + 10      # 3 + 10
print(f"num_3: {num_3}")
print(f"num_4: {num_4}")
# num_3: Number: 3
# num_4: Number: 13




## Vector final:
class Vector(MathStructure):
    shape = (None, )
    def __init__(self, values: list) -> None:
        self.values = values
        self.validate()
        self.length = self._get_len()
        self.shape = (self.length,)
        self.values = self.as_tuple()
    
    def _get_len(self) -> int:
        return len(self.values)
    
    def _get_mean(self) -> float:
        return round(sum(self.values) / self.length, 3)
    
    def _get_min(self)->Number:
        return min(self.values)
        
    def _get_max(self) -> Number:
        return max(self.values)
    
    def _get_range(self) -> Number:
        return max(self.values) - min(self.values)
    
    def get_stat(self) -> dict:
        """ calculate basic statistics """
        mean = self._get_mean()
        min_ = self._get_min()
        max_ = self._get_max()
        range_ = self._get_range()
        return {'mean': mean, 'min': min_, 
                'max': max_, 'range': range_}
        
    def __add__(self, other):
        if isinstance(other, Vector):
            if self.shape == other.shape:
                return Vector([x + y for x, y in zip(self.values, other.values)])
            else:
                raise ValueError(" Vectors must have same shape")
        elif isinstance(other, Number):
            return Vector([i + other for i in self.values])
        
    def __gt__(self, other):
        res_list = []
        if isinstance(other, Number):
            for item in self.values:
                res_list.append(item > other)
            return Vector(values=res_list)
        elif isinstance(other, Vector):
            if other.shape != self.shape:
                raise ValueError("Vectors must have same shape")
            else:
                for i in range(len(self.values)):
                    res_list.append(self.values[i] > other.values[i])
                return Vector(values=res_list)
        else:
            raise ValueError(f"Unsupported for {type(self)} and {type(other)}")
        
    # == üçün       
    def __eq__(self, other):
        res_list = []
        if isinstance(other, Number):
            for item in self.values:
                res_list.append(item == other)
            return Vector(values=res_list)
        elif isinstance(other, Vector):
            if other.shape != self.shape:
                raise ValueError("Vectors must have same shape")
            else:
                for i in range(len(self.values)):
                    res_list.append(self.values[i] == other.values[i])
                return Vector(values=res_list)
        else:
            raise ValueError(f"Unsupported for {type(self)} and {type(other)}")
    
    def __str__(self):
        return f"Vector: {self.values}"
           
    def __repr__(self):
        return self.__str__()
    
    

## Metaclasses
class MyMetaClass(type):
   def __new__(mcs, name, bases, attrs):
       print(f"MetaClass __new__ çağrıldı: {name} sinfi yaradılır.")
       print(f"  Valideynlər: {bases}")
       print(f"  Atributlar (ilkin): {attrs}")
       
       # Bütün atribut adlarını böyük hərfə çevirək (sadə bir nümunə)
       new_attrs = {}
       for attr_name, attr_value in attrs.items():
           if not attr_name.startswith("__"): # Dunder metodlara toxunmayaq
               new_attrs[attr_name.upper()] = attr_value
           else:
               new_attrs[attr_name] = attr_value
       
       print(f"  Yeni atributlar: {new_attrs}")
       # valideyn sinfə dəyişdirilmiş attributları göndəririk.
       return super().__new__(mcs, name, bases, new_attrs)
   
class SomeClass(metaclass=MyMetaClass):
   # belə bir sinif xüsusiyyəti olsun:
   some_prop = 10
   # və belə bir metod:
   def some_method(self):
       return "i am some method from SomeClass"

print("SomeClass nüsxəsi yaradılır...")
some_class_object = SomeClass()
print("some_class_object.: ", some_class_object.SOME_PROP)
print("some_class_object.SOME_METHOD(): ", some_class_object.SOME_METHOD())
# AttributeError: 'SomeClass' object has no attribute 'some_prop'
print("some_class_object.some_prop: ", {some_class_object.some_prop})

# MetaClass __new__ çağrıldı: SomeClass sinfi yaradılır.
#      Valideynlər: ()
#      Atributlar (ilkin): {'__module__': '__main__', '__qualname__': 'SomeClass', 'some_prop': 10, 'some_method': <function SomeClass.some_method at 0x796ae05a2340>}
#      Yeni atributlar: {'__module__': '__main__', '__qualname__': 'SomeClass', 'SOME_PROP': 10, 'SOME_METHOD': <function SomeClass.some_method at 0x796ae05a2340>}
# SomeClass nüsxəsi yaradılır...
# some_class_object.:  10
# some_class_object.SOME_METHOD():  i am some method from SomeClass





