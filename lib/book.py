#!/usr/bin/env python3

class Book:
    def __init__(self, title):
        self.title = title
        self._page_count = None
        # _page_count is a property and we make it a property when we want to 
        # place restrictions on what it can be 
        # the _ (underscore) denotes it as a property
        # we set it initialized to None rather than having a default value of 0
        # since we don't need to have a _page_count property to create an instance of Book
    
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) is int:
            self._page_count = page_count
        
        else:
            print(f"page_count must be an integer")
    
    page_count = property(get_page_count, set_page_count)
    
    def turn_page(self):
        print(f"Flipping the page...wow, you read fast!")
