outputHead = ['Student ID', 'Name', 'Total Scores/Assignments', 'Total Score', 'Average Score']

def openPrintList(file):
    with open(file, 'r') as f:
        of = f.readlines()
        f.close()

    return of

list1 = openPrintList('students.txt')
list2 = openPrintList('scores.txt')
print(list1,list2)

for element in list2:
    print(element)

for element in list1:
    print(element)


class Student:
    def __init__(self, name):
        self.name = name

    def add_assignment(self, assignment_name, score)
        self.assignment_name = name
        self.score = score
        
# thePrimagen/keyboards