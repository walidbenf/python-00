# Description: Write a function that takes an object and returns its type

def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(f"List : {type(object)}")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    elif isinstance(object, str):
        print(f"String : {type(object)}")
    else:
        print("Type not found")
    return 42
# isintance is a function that returns True,
# if the object is an instance of the class or subclass.
# Example : isinstance(1, int) returns True
