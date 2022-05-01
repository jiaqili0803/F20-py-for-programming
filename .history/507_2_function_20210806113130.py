#Functions make programs more readable

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

top_student = find_student_with_highest_average(students, grades)
print(top_student)


#Functions hide complexity
#Functions are reusable