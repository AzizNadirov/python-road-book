def divide(n, m):
    try:    # cəhd et
        return n / m
    except ZeroDivisionError:   # ZeroDivisionError baş verərsə
        print("You are dividing by zero!! ")
        return None

print(divide(25, 5))    # 5.0
print(divide(25, 0))    # 'You are dividing by zero!! '


## assert and raise
from typing import Union

def to_meter(value: Union[int, float], unit: str):
    # 'unit' kəmiyyəti və 1 unitin metrlərlə qiyməti 
    valid_units = {'km': 1000, 'dm': .1, 'mm': .001, 'm': 1, 
                   'mile': 1609.344, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254}
                   
    assert value > 0, "length must be a positive number."  # assert ilə yoxlama
    if not unit in valid_units.keys():  # adi şərt ilə yoxlama
        raise ValueError(f"unsupported unit - '{unit}'!\n" +
                         f"Possible units are: {list(valid_units.keys())}")
    
    one_in_m = valid_units[unit]    # 'one_in_m' - kəmiyyətin vahid metrdə dəyəri
    value_in_m = value * one_in_m 
    return value_in_m


print(to_meter(100, 'km'))  # 100000
print(to_meter(100, 'dm'))  # 10.0
print(to_meter(10, 'yard'))  # 9.144


