class Roster:
    def __init__(self):
        self.students = []

    def add(self, student):

        """
        Add a student to roster
        """
        self.students.append(student)

    def summarize(self):

        """
        Print students profile info
        """
        for student in self.students:
            print('Contact information for {0}. {1} is:'.
                    format(student.first_name[0], student.last_name))
            student.print_info()