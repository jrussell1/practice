from helpers import *

students = []

while True:
    # Get information and assign via unpacking. Order matters.
    first, last, middle, address, email, phone = get_student_information()

    # Create a student by passing kwargs. We can do this with positional
    # arguments, as well, but this is arguably more robust.
    student = create_student(first_name = first, last_name = last,
            middle_initial = middle, address = address, email = email,
            phone_number = phone)
    
    print_student(student)
    
    # Prompt for confirmation. Use lower so users can enter either Y or y.
    if confirm('Is this information correct? (Y/n) '):
        students.append(student)
        
        if confirm('Would you like to input another student\'s information? (Y/n) '):
            continue
        else:
            print_summary(students)
            break
