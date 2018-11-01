#!/usr/bin/python3

from helpers import *

from Roster import Roster

from Student import Student

###############################################################################
#
# BRIEF //
#   We'll implement just one more refactor before we call it a day. For this
#   activity, you'll need to:
#
#     1. Implement a Student class. This will be in Student.py, and replace
#        the dictionary you're currently using to store student information.
#        Equip it with a "report" method that prints student information the
#        way you currently do just before asking users for confirmation.
#
#    2. Implement a Roster class. This is just a simple wrapper around the 
#       array you're currently using. Equip it with its own "report" method,
#       which prints each student's information iteratively.
#
#    3. Finally, make the appropriate imports and substitutions in your script
#       to clean it up. This part should be relatively straightforward.
#
###############################################################################
roster = Roster()

while True:
    # Get information and assign via unpacking. Order matters.
    first, last, middle, address, email, phone = get_student_information()
    student = Student(first, last, middle, address, email, phone)
    # Create a student by passing kwargs. We can do this with positional
    # arguments, as well, but this is arguably more robust.
    
    
    student.print_info()
    
    # Prompt for confirmation. Use lower so users can enter either Y or y.
    if confirm('Is this information correct? (Y/n) '):
        roster.add(student)
        
        if confirm('Would you like to input another student\'s information? (Y/n) '):
            continue
        else:
            roster.summarize()
            break
