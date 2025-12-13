# functools

import functools
import time


## cache

def my_sum_cacher(arr, delay=0):
    time.sleep(delay)
    return sum(arr)


def casher(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@casher
def my_sum_cacher(arr, delay=0):
    time.sleep(delay)
    return sum(arr)

my_sum_cacher((1,2,3), delay=2) # 2 san
my_sum_cacher((1,2,3), delay=2) # 0 san



from collections import OrderedDict
    
def casher_lru(maxsize=128):
    def decorator(func):
        cache = OrderedDict()
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if key in cache:
                cache.move_to_end(key)
            else:
                if len(cache) >= maxsize:
                    cache.popitem(last=False)
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper
    return decorator


@casher_lru(maxsize=2)
def my_sum_lru(arr, delay=0):
    time.sleep(delay)
    return sum(arr)

print(my_sum_lru((1,2,3), delay=2)) # 2 san
print(my_sum_lru((1,2,1), delay=2)) # 0 san
print(my_sum_lru((1,2,3), delay=2)) # 2 san



import functools, time

@functools.lru_cache(maxsize=128)
def my_sum_lru(arr, delay=0):
    time.sleep(delay)
    return sum(arr)

print(my_sum_lru((1,2,3), delay=2)) # 2 san
print(my_sum_lru((1,2,1), delay=2)) # 0 san
print(my_sum_lru((1,2,3), delay=2)) # 2 san




## partial

def power(base, exponent):
   return base ** exponent

def partial(func, *args, **kwargs):
    def wrapper(*more_args, **more_kwargs):
        return func(*args, *more_args, **{**kwargs, **more_kwargs})
    return wrapper


square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(3))  # 9
print(cube(3))    # 27




## overloading

import functools
   
@functools.singledispatch
def my_sum(arg):
   print("Unknown type")
   raise NotImplementedError("Unsupported type")

@my_sum.register
def mysum_list(arg: list):
   print("summing for list")
   return sum(arg)

@my_sum.register
def mysum_dict(arg: dict):
   print("summing for dict values")
   return sum(arg.values())

print(my_sum([1, 2, 3]))
print(my_sum({"a": 1, "b": 2, "c": 3}))
print(my_sum(1))  # raise NotImplementedError

# summing for list
# 6
# summing for dict values
# 6
# Unknown type
# ...
#  3 @functools.singledispatch
#          4 def my_sum(arg):
#          5     print("Unknown type")
#    ----> 6     raise NotImplementedError("Unsupported type")
   
#    NotImplementedError: Unsupported type





import functools
from typing import Union

@functools.singledispatch
def my_sum(arg):
   print("Unknown type")
   raise NotImplementedError("Unsupported type")

@my_sum.register
def _(arg: list):
   print("summing for list")
   return sum(arg)

@my_sum.register
def _(arg: dict):
   print("summing for dict values")
   return sum(arg.values())

@my_sum.register
def _(arg: int | float):
   print("summing for int")
   return arg

@my_sum.register
def _(arg: Union[set, tuple]):
   print("summing for set or tuple")
   return sum(arg)

print(my_sum([1, 2, 3]))
print(my_sum({"a": 1, "b": 2, "c": 3}))
print(my_sum(5))
print(my_sum({1, 2, 3}))
print(my_sum((1, 2, 3)))
print(my_sum("hello"))  # NotImplementedError: Unsupported type 

# summing for list
# 6
# summing for dict values
# 6
# summing for int
# 5
# summing for set or tuple
# 6
# summing for set or tuple
# 6
# Unknown type


### using explicit - lambda
my_sum.register(type(None), lambda arg: print("summing for None "))
my_sum(None)  # summing for None type