# itertools


from itertools import accumulate
from typing import Iterator


numbers = [1, 2, 3, 4, 5]
print(list(accumulate(numbers)))  
# [1, 3, 6, 10, 15]

def custom_accumulate(iterable, func:callable=sum)->Iterator:
    """ custom accumulate function """
    for i in range(len(iterable)):
        yield func(iterable[:i+1])

print(custom_accumulate(numbers))
# <generator object custom_accumulate at 0x7502c62bee40>
print(list(custom_accumulate(numbers)))
# [1, 3, 6, 10, 15]




def custom_accumulate(iterable, func:callable=sum)->Iterator:
    """ custom accumulate function """
    for i in range(len(iterable)):
        yield func(iterable[:i+1])

print(custom_accumulate(numbers))
# <generator object custom_accumulate at 0x7502c62bee40>
print(list(custom_accumulate(numbers)))
# [1, 3, 6, 10, 15]


def custom_accumulate_optimized(iterable, func=lambda x, y: x + y):
   """ custom accumulate function """
   # iteratora çevirək. Hər dəfə next ilə element aldıqda +1 addım atmlş olacağıq.
   iterator = iter(iterable)
   try:
       # ilk next, ilk elementi alırıq
       accumulated = next(iterator)
       yield accumulated
       # növbə ilə digərləri üçün də hesablayırıq.
       for item in iterator:
           accumulated = func(accumulated, item)
           yield accumulated
   except StopIteration:
       # iterator boşdursa, sadəcə None qaytaraq
       return None
   
   numbers = [1, 2, 3, 4, 5]
   print(list(custom_accumulate_optimized(numbers)))
   # [1, 3, 6, 10, 15]