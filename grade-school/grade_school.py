from collections import defaultdict

class School():

    def __init__(self):
        # initialize students as a defaultdict with a list to hold names of students
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        roster = []
        grade_list = []
        for entry in self.students.items():
            entry[1].sort()
            grade_list.append(entry)
        grade_list.sort()
        final = [x[1] for x in grade_list]
        return [x for x in final for x in x]

    def grade(self, grade_number):
        return sorted(self.students[grade_number])
