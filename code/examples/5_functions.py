# 5 - Functions

## just return
def average(a, b, c):
    s = a + b + c
    return s / 3

# return and print
def average(a, b, c):
    s = a + b + c
    return s / 3
print(average(3, 3, 6) * 10)    # 40


def average(nums):
    s = sum(nums)
    ln = len(nums)
    return s / ln

average([1,2,3,4,5])    # 3.0

## shorter
def average(nums):
    return sum(nums) / len(nums)
average([1,2,3,4,5])   # 3.0



## find item in array
def find(array, item):
    i = 0
    while i < len(array):
        if array[i] == item:  # element tapıldı
            return i          # qaytar
        else:
            i += 1   # tapılmasa, i = i+1, əks halda sonsuz dövü yaranacaq
    else:
        return -1

array = [2, 7, 8, 9, 11]
print(find(array, 2))    # 0
print(find(array, 8))    # 2


## capitalise all words
def capitalise_all(words):
    capitalised_names = [word.capitalize() for word in words]
    return capitalised_names
	
names = capitalise_all(['anar', 'ayan', 'arzu'])
cities = capitalise_all(['baku', 'ganja', 'barda'])
print(names)   # ['Anar', 'Ayan', 'Arzu']
print(cities)  # ['Baku', 'Ganja', 'Barda']



## word counter
sentence_1 = "Aşbaz aşbaz aş asmış asmışsa da az asmış aş asmış"
sentence_2 = "bir bir gəlin bir bir gedin"

def count_words(sentence):
    sentence = sentence.lower()  # hərfləri kiçik et
    words = sentence.split(' ')  # cümləni sözlərə parçala
    word_count = {}   # boş lüğət
    for word in words:    # sözlər siyahısını iterə edək
        if not word in word_count:
            word_count[word] = 1   # hələ əlavə edilməyibsə əlavə et
                                   # dəyərini 1 kimi təyin et
        else:                # əks halda dəyərini al və
            word_count[word] = word_count[word] + 1    # 1 vahid artır
    return word_count
	
print(count_words(sentence_1))
# {'aşbaz': 2, 'aş': 2, 'asmış': 3, 'asmışsa': 1, 'da': 1, 'az': 1}
print(count_words(sentence_2))
# {'bir': 4, 'gəlin': 1, 'gedin': 1}


## Nested functions
def salam_sagol(ad):
    # iç funksiya 1
    def salamla(ad):
        print(f"Salamlar olsun - {ad} ")
    # iç funksiya 2
    def sagollas(ad):
        print(f"Görüşənədək - {ad}")
        
    # salamlaş
    salamla(ad)
    # sağollaş
    sagollas(ad)

salam_sagol("Əziz")
# Salamlar olsun - Əziz
# Görüşənədək - Əziz



## calculator function
def calc(num_1, num_2, operation):
    # mövcud əməliyyatlar
    operations = ('+', '-', '*', '/')
    # hesablayıcı funksiyalar
    def add(num_1, num_2):
        return num_1 + num_2
    def sub(num_1, num_2):
        return num_1 - num_2
    def mul(num_1, num_2):
        return num_1 * num_2
    def divide(num_1, num_2):
        return num_1 / num_2
        
    # əməliyyatın düzgünlüyünü yoxla
    if not operation in operations:
        print(f"Yanlış əməliyyat: '{operation}'. Düzgün əməliyyatlar: \
        {operations}")
        return None
    else:
        if operation == '+':
            res = add(num_1, num_2)
        elif operation == '-':
            res = sub(num_1, num_2)
        elif operation == '*':
            res = mul(num_1, num_2)
        elif operation == '/':
            res = divide(num_1, num_2)
    return res
	
print(calc(5, 5, '+'))    # 10
print(calc(5, 5, '-'))    # 0
print(calc(5, 5, '*'))    # 25
print(calc(5, 5, '/'))    # 1.0


## calculator func V2
def calc(num_1, num_2, operation):
    # hesablayıcı funksiyalar
    def add(num_1, num_2):
        return num_1 + num_2
        
    def sub(num_1, num_2):
        return num_1 - num_2
        
    def mul(num_1, num_2):
        return num_1 * num_2
        
    def divide(num_1, num_2):
        return num_1 / num_2
        
    # mövcud əməliyyatlar: açar - əməliyyat, dəyər - əməliyyata cavabdeh funksiya
    operations = {'+': add, '-': sub, '*': mul, '/': divide}
    # əməliyyatın düzgünlüyünü yoxla
    if not operation in operations.keys():
        print(f"Yanlış əməliyyat: '{operation}'. Düzgün əməliyyatlar:\
        {operations}")
        return None
    else:
        func = operations[operation]
        res = func(num_1, num_2)
        return res
		
print(calc(5, 5, '+'))   # 10
print(calc(5, 5, '-'))   # 0
print(calc(5, 5, '*'))   # 25
print(calc(5, 5, '/'))   # 1.0


## custom power function
def my_pow(base, power, mod=None):
    if mod is None:
        return base ** power
    else:
        return (base ** power) % mod

print(my_pow(2, 4, 5))   # 1
print(2, 4)              # 16


## email generator function
def generate_email(name, surname, separator='', domain='fake.com'):
    return f"{name}{separator}{surname}@{domain}"
	
print(generate_email("aziz", "nadirov")) # 'aziznadirov@fake.com'
print(generate_email("aziz", "nadirov", '_')) # 'aziz_nadirov@fake.com'
print(generate_email("aziz", "nadirov", '_', 'ml.com')) # 'aziz_nadirov@ml.com'


## function with default value
def calc(a, b, operator='+'):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return None
    
print(calc(2, 3))                   # 5
print(calc(2, 3, operator='*'))     # 6



## 
employees = [
       {'id': 0, 'first_name': 'Aziz', 'last_name': 'Nadirov', 
       'age': 25, 'salary': 1500},
       {'id': 1, 'first_name': 'Aziz', 'last_name': 'Nadirli', 
       'age': 26, 'salary': 1500},
       {'id': 2,'first_name': 'Den', 'last_name': 'Bruk', 
       'age': 30, 'salary': 2000},
       {'id': 3,'first_name': 'Leyla', 'last_name': 'Rahimova', 
       'age': 26, 'salary': 1400},
   ]
   
def search_employee(employees, name=None, age=None, salary=None, only_id=False):
    if name == age == salary == None:
       print("All parameters are None")
       return None

    found = []
    for employee in employees:
        if name and employee['first_name'] != name:
            continue
        if age and employee['age'] != age:
            continue
        if salary and employee['salary'] != salary:
            continue
        found.append(employee)
    
    # belə
    if only_id:
        return [employee['id'] for employee in found]
    else:
        return found
    
    # ya da qısaca belə: 
    # return [employee['id'] for employee in found] if only_id else found


print(search_employee(employees, name="Aziz"))
# out
# [{'id': 0, 'first_name': 'Aziz', 'last_name': 'Nadirov', 'age': 25, 'salary': 1500}, 
#  {'id': 1, 'first_name': 'Aziz', 'last_name': 'Nadirli', 'age': 26, 'salary': 1500}]
print(search_employee(employees, name="Aziz", only_id=True))
# [0, 1]
print(search_employee(employees, name="Aziz", age=25))
# [{'id': 0, 'first_name': 'Aziz', 'last_name': 'Nadirov', 'age': 25, 'salary': 1500}]



## 5.9

def make_discounter(percent):
    def discounter(price):
        return price - (price * (percent/100))
        
    if percent < 0:
        print(f"negaitive value for percent.")
        return None
    # if ödəndiyi təqdirdə funksiya bitir, odur ki 'else' yazmasaq da olar
    return discounter

# 'endirimçi' funksiyalar
do_10 = make_discounter(percent=10)     # 10 faiz
do_50 = make_discounter(percent=50)     # 50 faiz
do_100 = make_discounter(percent=100)   # 100 faiz - pulsuz apar

print(do_10(1000))  # 900.0
print(do_50(1000))  # 500.0
print(do_100(1000)) # 0.0


## 5.10
products = [
    {'id': 1, 'name': 'smartfon iphone 99 pro',  'category': 'smartphone', 'price': 10000},
    {'id': 2, 'name': 'smartfon xiaomi poco M5 128',  'category': 'smartphone', 'price': 400},
    {'id': 3, 'name': 'lenovo legion 5',  'category': 'laptops', 'price': 2000},
    {'id': 4, 'name': 'laptop dell inspiron 15',  'category': 'laptops', 'price': 1200},
    {'id': 5, 'name': 'airpods 99',  'category': 'headphones', 'price': 300},
]

def get_price(id, products):
    # id-ə uyğun elementlər siyahı şəklində qaytarılır
    return [p['price'] for p in products if p['id'] == id]

get_price(id=2, products=products)   # [400]


def with_discount(foo):
    def wrapper(id, products):
        res = foo(id, products)
        p = 0.5      # 50%
        res = [r - (p*r) for r in res]    # hər bir nəhsul üçün endirim
        return res
    
    return wrapper

def get_price(id, products):
    # id-ə uyğun elementlər siyahı şəklində qaytarılır
    return [p['price'] for p in products if p['id'] == id]

# endirimləşdirilmiş 'get_price' əldə edək
get_price_50 = with_discount(get_price)
# 2 id-li məhsul üçün
get_price_50(id=2, products=products)    #[200.0]

## with @
@with_discount
def get_price(id, products):
    # id-ə uyğun elementlər siyahı şəklində qaytarılır
    return [p['price'] for p in products if p['id'] == id]


# dekorator
def with_discount_2(foo):
    discounts = {1: 0.50, 2: 0.50, 3: 0.20, 4: 0.10}
    def wrapper(id_, products):
        res = foo(id_, products)
        p = discounts.get(id_, 0)     # 'id' endirimdə olmasa, 'get' 0 qaytacaq
        res = [r - (p*r) for r in res]    # hər bir nəhsul üçün endirim
        return res
    
    return wrapper

# dekorlanmış funksiya
@with_discount_2
def get_price(id_, products):
    # id-ə uyğun elementlər siyahı şəklində qaytarılır
    return [p['price'] for p in products if p['id'] == id_]

print(get_price(id_=1, products=products))      # [5000.0]  -50%
print(get_price(id_=3, products=products))      # [1600.0]  -20%
print(get_price(id_=5, products=products))      # [300.0]   -0%



### parameterised decorators
def apply_discount(discounts_dict):
    def inner(foo):
        def wrapper(id_, products):
            res = foo(id_, products)
            p = discounts_dict.get(id_, 0)    # 'id' endirimdə olmasa, 'get' 0 qaytacaq
            res = [r - (p*r) for r in res]    # hər bir nəhsul üçün endirim
            return res
        
        return wrapper
    
    return inner

@apply_discount(discounts_dict={1: 0.50, 2: 0.50, 3: 0.20, 4: 0.10})
def get_price(id_, products):
    # id-ə uyğun elementlər siyahı şəklində qaytarılır
    return [p['price'] for p in products if p['id'] == id_]

print(get_price(id_=1, products=products))      # [5000.0]  -50%
print(get_price(id_=3, products=products))      # [1600.0]  -20%
print(get_price(id_=5, products=products))      # [300.0]   -0%



## generators

def get_fibo():
    # ilk 2 elementi əl ilə doldurmuşam
    sequence = [1, 1, ]
    for i in sequence:
        yield i
        
    # sonrakıları dövr daxilində
    i=1
    while True:     # sonsuz dövr
        num = sequence[i] + sequence[i-1]
        sequence.append(num)
        i += 1
        yield sequence
        
fibo = get_fibo()   # generator
for i in range(1, 11):
    print(f"[{i}]: {next(fibo)}")

# [1]: 1
# [2]: 1
# [3]: [1, 1, 2]
# [4]: [1, 1, 2, 3]
# [5]: [1, 1, 2, 3, 5]
# [6]: [1, 1, 2, 3, 5, 8]
# [7]: [1, 1, 2, 3, 5, 8, 13]
# [8]: [1, 1, 2, 3, 5, 8, 13, 21]
# [9]: [1, 1, 2, 3, 5, 8, 13, 21, 34]
# [10]: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def get_fibo(n):
    # n elementli fibo ardıcıllığı
    # ilk 2 elementi əl ilə doldurmuşam
    if n < 1: return None   # yanlış n
    if n == 1: return 1
    elif n == 2: return [1, 1, ]
    sequence = [1, 1, ]    
    for i in sequence:
        yield i
    # sonrakıları dövr daxilində
    for i in range(1, n-2): # iki iterasiya artıq yuxarıda edilib
        num = sequence[i] + sequence[i-1]
        sequence.append(num)
        yield sequence
        
for i, fibo_i in enumerate(get_fibo(11), start=1):
    print(f"[{i}]: {fibo_i}")
    

# [1]: 1
# [2]: 1
# [3]: [1, 1, 2]
# [4]: [1, 1, 2, 3]
# [5]: [1, 1, 2, 3, 5]
# [6]: [1, 1, 2, 3, 5, 8]
# [7]: [1, 1, 2, 3, 5, 8, 13]
# [8]: [1, 1, 2, 3, 5, 8, 13, 21]
# [9]: [1, 1, 2, 3, 5, 8, 13, 21, 34]
# [10]: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


## yield from
def generator1():
    for i in [1,2,3]:
        yield i

def generator2():
    for i in ['a', 'b', 'c']:
        yield i

def mega_generator():
    yield from generator1()
    yield from generator2()

for i in mega_generator():
    print(i, end=',')     # 1,2,3,a,b,c,