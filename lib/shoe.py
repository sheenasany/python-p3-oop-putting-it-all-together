#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        self._size = None
        # _size is a property and we make it a property when we want to 
        # place restrictions on what it can be 
        # the _ (underscore) denotes it as a property
        # we set it initialized to None rather than having a default value of 0
        # since we don't need to have a _size property to create an instance of Shoe
    def get_int_size(self):
        return self._size
    
    def set_int_size(self, size):
        if type(size) is int:
            self._size = size
        
        else:
            print(f"size must be an integer")
    
    size = property(get_int_size, set_int_size)
    
    def cobble(self):
        print(f"Your shoe is as good as new!")
        self.condition = "New"