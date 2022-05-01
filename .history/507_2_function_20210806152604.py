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
