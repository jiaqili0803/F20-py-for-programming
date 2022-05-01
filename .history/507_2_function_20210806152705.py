#Functions make programs more readable
#Functions hide complexity

'''students = {
    '1001': {'last_name': 'Newman', 'first_name': 'Mark', 'uniqname': 'mwnewman'},
    '1002': {'last_name': 'Kano', 'first_name': 'Tsuyoshi', 'uniqname': 'tkano'},
    '1003': {'last_name': 'Grill', 'first_name': 'Gabriel', 'uniqname': 'ggrill'},
    '1004': {'last_name': 'Chen', 'first_name': 'Kangning', 'uniqname': 'knchen'}
}
grades = {
    '1001': [90, 88, 75, 95],   
    '1002': [92, 99, 88, 100],
    '1003': [95, 88, 82, 100],
    '1004': [99, 92, 94, 98]
}

def find_student_with_highest_average(students, grades):
  max = 0
  max_id = -1
  for id in grades: #循环每个人
      sum = 0
      num_grades = 0
      for g in grades[id]:
          sum += g
          num_grades += 1
      avg = sum/num_grades #每个学生平均分
      if avg > max:
          max = avg
          max_id = id
  return students[max_id] #return平均分最高的学生

top_student = find_student_with_highest_average(students, grades)
print(top_student)'''



#Functions are reusable-Don’t Repeat Yourself.
# lec2_1.py

students = {
    '1001': {'last_name': 'Newman', 'first_name': 'Mark', 'uniqname': 'mwnewman'},
    '1002': {'last_name': 'Kano', 'first_name': 'Tsuyoshi', 'uniqname': 'tkano'},
    '1003': {'last_name': 'Grill', 'first_name': 'Gabriel', 'uniqname': 'ggrill'},
    '1004': {'last_name': 'Chen', 'first_name': 'Kangning', 'uniqname': 'knchen'}
}

grades = {
    '1001': [90, 88, 75, 95],   
    '1002': [92, 99, 88, 100],
    '1003': [95, 88, 82, 100],
    '1004': [99, 92, 94, 98]
}

def find_student_with_highest_average(students, grades):
    max = 0
    max_id = -1
    for id in grades:
        sum = 0
        num_grades = 0
        for g in grades[id]:
            sum += g
            num_grades += 1
        avg = sum/num_grades
        if avg > max:
            max = avg
            max_id = id
    return students[max_id]

def compute_final_grades(grades):
    student_grades = {}
    for id in grades:
        sum = 0
        num_grades = 0
        for g in grades[id]:
            sum += g
            num_grades += 1
        student_grades[id] = sum/num_grades
    return student_grades

def print_final_grades(students, final_grades):
    for id in final_grades:
        student = students[id]
        print(student['first_name'], student['last_name'], 'has', final_grades[id])

top_student = find_student_with_highest_average(students, grades)
print("The top student is", top_student['first_name'], top_student['last_name'])

final_grades = compute_final_grades(grades)
print_final_grades(students, final_grades)