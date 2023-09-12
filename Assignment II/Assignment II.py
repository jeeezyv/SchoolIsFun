# This module contains the People class, which is used to create a list of people and the different types of people in our system
# Create a class called Person which is the base class from which other classes will inherit
class Person:

    # Creating the properties of the Person class
    id = 0
    first_name = ""
    last_name = ""
    
    # A person has an ID, first name and last name 
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    # The id property is a unique identifier for each person
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        # Check if the id is a positive integer, if not raise an exception
        if id < 0:
            raise ValueError("ID must be a positive integer")
        self.id = id

    # The string representation of a person is their first name and last name
    def __str__(self):
        return f'{self.first_name} {self.last_name}'