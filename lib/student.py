#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Initialize the parent User class
        self.knowledge = []  # Initialize an empty knowledge list

    def learn(self, new_knowledge):
        # Add new knowledge to the student's knowledge list
        self.knowledge.append(new_knowledge)
