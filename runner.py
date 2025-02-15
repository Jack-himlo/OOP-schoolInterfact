from classes.school import School 

school = School('Ridgemont High') 

# print(school.name)
# print(school.staff)
# print(school.students)


#show "interface" and expect user input/option
mode =input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
print(mode)

if mode == '1':
    print("List of all students:")
    for student in school.students:
        print(f"{student.name} {student.school_id}")
elif mode == '2':
    student_id = input("enter student id: ")
    for student in school.students:
        if student_id == student_id:
            print(f"student id: {student_id}'s name is {student.name}")
            break
        else:
            print(f"There was no student found with that ID.")
    # student = school.student.school_id(student_id)
    # print(student)
elif mode == '3':
    pass
elif mode == '4':
    pass
elif mode == '5':
    pass
elif mode == '6':
    pass
else:
    pass 

