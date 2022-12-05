# David Liddle              # 12-1-22
# Lab 15 Exercise 1

def open_print_list(file):
    with open(file, 'r') as f:
        of = f.readlines()
        f.close()
    return of

def extract_student_data(students_dict, student_data_list):
    for i in range(1, len(student_data_list)):
        interim_list = student_data_list[i].split(',')
        students_dict[interim_list[0]] = [(interim_list[1].rstrip()).strip(),0,0,0]
    return students_dict    

def extract_student_assignemnts(students_dict, student_assignments_list):
    for i in range(1, len(student_assignments_list)):
        interim_list = student_assignments_list[i].split(',')
        students_dict[interim_list[0]][1] += 1
        students_dict[interim_list[0]][2] += int(interim_list[2].rstrip())
    return students_dict

def compute_average(students_dict):
    keys_list = students_dict.keys()
    for elem in keys_list:
        num_assns = students_dict[elem][1]
        total_score = students_dict[elem][2]
        avg_score = total_score/num_assns
        formatted_avg_score = '{:.1f}'.format(avg_score)
        students_dict[elem][3] = formatted_avg_score
        students_dict[elem][1] = str(num_assns)
        students_dict[elem][2] = str(total_score)
    return students_dict     
 
def create_grades_file():
    header_string = 'Student ID,Name,Total Scores,Sum of All Scores,Score Average'
    with open('grades.txt', 'w') as f:
        f.write(header_string)
        f.write('\n')
        f.close()

def append_output_lines(students_dict):
    keys_list = []
    for key in students_dict:
        keys_list.append(key)
    for elem in keys_list:
        interim_list = students_dict[elem]
        interim_list.insert(0, elem)
        append_string = ','.join(interim_list)
        with open('grades.txt', 'a') as f:
            f.write(append_string)
            if keys_list.index(elem) != len(keys_list)-1:
                f.write('\n')
                f.close()
            else:
                f.close()

students = {}
list1 = open_print_list('students.txt')
list2 = open_print_list('scores.txt')
students_step_1 = extract_student_data(students, list1)
students_step_2 = extract_student_assignemnts(students_step_1, list2)
students_step_3 = compute_average(students_step_2)
create_grades_file()
append_output_lines(students_step_3)

list3 = open_print_list

'''
    student_dictionary_structure = {
        '123456': [name, total_assignments, total_points, avg_points]
        ...  
    }

['Student ID, Name\n', 
'123456, John Smith\n', 
'654321, John Smith\n', 
'246810, Trevor Smith\n', 
'135791, Sally Smith']

['Student ID, Assignment, Score\n', 
'123456, Zany Text, 100\n', 
'123456, Magic 9 Ball, 60\n', 
'123456, Nim Grab, 80\n', 
'123456, Dungeon Crawl, 78\n', 
'123456, Ultimate TODO List, 90\n', 
'654321, Zany Text, 48\n', 
'654321, Ultimate TODO List, 82\n', 
'654321, Nim Grab, 17\n', 
'246810, Zany Text, 100\n', 
'246810, Ultimate TODO List, 24\n', 
'246810, Nim Grab, 98\n', 
'135791, Zany Text, 84\n', 
'135791, Ultimate TODO List, 3\n', 
'135791, Nim Grab, 89\n', 
'135791, Dungeon Crawl, 0']

with open('grades.txt','w') as f:
    f.write(header_line)
    f.close()
'''