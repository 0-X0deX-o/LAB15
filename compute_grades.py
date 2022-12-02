# David Liddle              # 12-1-22
# Lab 15 Exercise 1

outputHead = ['Student ID', 'Name', 'Total Scores/Assignments', 'Total Score', 'Average Score']

def openPrintList(file):
    with open(file, 'r') as f:
        of = f.readlines()
        f.close()

    return of

list1 = openPrintList('students.txt')
list2 = openPrintList('scores.txt')
header_line = ', '.join(outputHead)
with open('grades.txt','w') as f:
    f.write(header_line)
    f.close()

for i in range(1, len(list1)):
    students = []
    students.append({list1[i][0]:[list1[i][1],0,0,0]})
    for j in range(1, len(list1)):
        if list2[j][0] == students[i - 1][list1[i][0]]:
            students[i - 1][list1[i][0]][1] += 1
            students[i - 1][list1[i][0]][2] += list2[j][2]
    students[i - 1][list1[i][0]][3] = students[i - 1][list1[i][0]][2]/students[i - 1][list1[i][0]][1]
    output_line = ', '.join(students)
    with open('grades.txt', 'a') as a:
        a.write(output_line)
        a.close()



'''
    global()[f'_{id}'.format()] = new Student(id, name)    

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.assignments = {}
        self.num_assns = 0
        self.scores = []
        self.average_score = 0
        self.total_score = 0
    def add_assignment(self, assignment_name, score):
        self.assignments[assignment_name] = score
        self.num_assns  += 1
        
    def create_scores_list(self, assignments_dict):
        self.scores = list(assignments_dict.values())
    def sum_scores(self, scores_list):
        sum_total = 0
        for i in range(0, len(scores_list)):
            sum_total += scores_list[i]
        self.total_score = sum_total
    def compute_average(self, total_assignments, total_score):
        self.average_score = total_assignments / total_score
        
for elem in list1:
    compVar = '_' + str(elem[0]) 
    eval(compVar) = new Student(elem[0], elem[1])
    
for elem in list2:
    compVar = '_' + str(elem[0])
    eval(compVar).add_assignment(elem[1], elem[2])
header_string = ', '.join(outputHead) 
with open('grades.txt', 'w') as f:
    f.write(header_string)
    f.close()
for elem in list1:
    output_list = []
    compVar = '_' + str(elem[0])
    vr = eval(compVar)
    output_list.append(str(vr.id))
    output_list.append(str(vr.name))
    output_list.append(str(vr.create_scores_list(vr.assignments)))
    output_list.append(str(vr.sum_scores(vr.scores)))
    output_list.append(str(vr.compute_average(vr.num_assns, vr.total_score)))
    output_line  = ', '.join(output_list)
    with open('grades.txt', 'a') as f:
        f.write(output line)
        f.close()
'''
