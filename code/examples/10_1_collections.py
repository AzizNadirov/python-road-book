## Collections


from typing import Sequence, Optional, Any, Union, Tuple
from collections import deque
   
class Stack:
   """ class simulates a stack based on the que """
   def __init__(self, 
                items: Optional[Sequence]=None,
                max_length: Optional[int]=None):
       """
       Args:
           - items: stack initial items
           - max_length - maximum length of the stack
       """
       self.__items = deque(items or (), maxlen=max_length)
       self.__max_len = max_length
   
   def retrieve(self)->Union[Any, None]:
       """ retrieve item from the stack """
       if len(self.__items) > 0:
           return self.__items.pop()
       print("Stack is empty!")
       return None
       
   def add(self, item_to_add: Any) -> bool:
       """ add new item to the stack """
       if len(self.__items) == self.__max_len:
           print("Stack is full!")
           return False
       self.__items.append(item_to_add)
       print(f"{item_to_add} added to stack: {self.get_stack()}")
       return True
   
   def get_stack(self)->Tuple[Any]:
       """ get stack items as a tuple """
       return tuple(self.__items)
   
   def clear(self) -> None:
       self.__items.clear()
       print("Stack is clean!")
   
   def __str__(self):
       return str(self.get_stack())

stack = Stack(items=[1,2], max_length=4)
stack.add(3)
stack.retrieve()
stack.add(3)
stack.add(3)
stack.add(3)
print(f"stack: {stack}")
stack.clear()
print(f"stack after clear: {stack}")        


# 3 added to stack: (1, 2, 3)
# 3 added to stack: (1, 2, 3)
# 3 added to stack: (1, 2, 3, 3)
# Stack is full!
# stack: (1, 2, 3, 3)
# Stack is clean!
# stack after clear: ()


