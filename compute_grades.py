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

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.assignments = {}
        self.num_assns = 0
        self.scores = []

    def add_assignment(self, assignment_name, score):
        self.assignments[assignment_name] = scores
        self.num_assns  += 1
        
    def output_stats(self, assignments_dict):
        self.scores = list(assignment_dict.values())

    def 
# thePrimagen/keyboards