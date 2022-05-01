## Writing Good Functions
    #use clear names (long and clear is better than short and cryptic)
        #Find-and-replace function、refactor commands来全部替换名称
    #The Single Responsibility Rule
        #一个funct就做一件事，可以分别多分几个funct达成目的，更简洁
        #def compute_average(num_list):   
        #def calculate_student_averages(students, grades): 
        #def find_student_with_highest_average(students, grades):
    #Keep a Function Short（<50 lines）
    #Avoid Side Effects
        #changes should be restricted to the function’s return value
        #are not expected to modify the inputs and global variables
    #Towards More “Pure” Functions（可以这么纯，但也不必追求极致）
        #不影响外部的任何数据（通过 return 除外），也不应更改其外部的任何数据，例如全局变量（通过其参数除外）
        import copy #纯粹到需要 copy一个新的students副本而不对原有的students做改动
        def calculate_student_averages(students, grades):
            students_copy = copy.copy(students)
            for id in grades:
                students_copy[id]["average"] = compute_average(grades[id])
            return students_copy
        updated_students = calculate_student_averages(students, grades)
    #Document Your Functions
        #always comment your functions!
        #可以用doc-str:
        def find_student_with_highest_average(students, grades):
            '''takes a dictionary of students of the form
                {id: {student_info}, ...} and a dictionary of grades 
                of the form {id: [list_of_grades]}. 

                Calculates averages for each student, then returns
                the student ({student_info}) of the student with the 
                highest average.

                Note: results are indeterminate in the case of two top students 
                tied for the highest average. 
            '''
            max = 0
            top_student = None
            calculate_student_averages(students, grades)
            for s in students.values():
                if s["average"] > max:
                    max = s["average"]
                    top_student = s
            return top_student
        # Numpy doc-str format: (main 4 parts：Summary、Extended description、Parameters、Returns)
        def the_func(arg1, arg2):
            '''Summary line.

                Extended description of function.

                Parameters
                ----------
                arg1 : int
                    Description of arg1
                arg2 : str
                    Description of arg2

                Returns
                -------
                bool
                    Description of return value
                '''
        #用Numpy doc-str format举例写一个docstr:        
        def find_student_with_highest_average(students, grades):
            '''find student with the best average grade in the class
                
                takes a dictionary of students and a dictionary of grades,  
                calculates averages for each student, then returns
                the info of the student with the highest average.
                
                Note: results are indeterminate in the case of two top students 
                tied for the highest average. 

                Parameters
                ----------
                students : dict
                    student info, indexed by id {id: {student_info}, ...}
                grades : dict
                    student grades, indexed by id {id: [list_of_grades], ...}
                Returns
                -------
                dict
                    the student info (name, email, etc.) of the student with the highest average
            '''
            max = 0
            top_student = None
            calculate_student_averages(students, grades)
            for s in students.values():
                if s["average"] > max:
                    max = s["average"]
                    top_student = s
            return top_student