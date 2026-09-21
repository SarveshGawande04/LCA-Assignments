# Assignment 1: Student Data Management

# Tuples
student1 = ("Rahul", "CSE", 85)
student2 = ("Amit", "ECE", 78)
student3 = ("Sneha", "AI & DS", 92)

# List
student_list = [student1, student2, student3]

# Dictionary
students = {
    1: student1,
    2: student2,
    3: student3
}

# Display original records
print("Student Records:")


for roll_no, details in students.items():
    print("Roll No:", roll_no)
    print("Name:", details[0])
    print("Branch:", details[1])
    print("Marks:", details[2])
    


# Add a new student
students[4] = ("Priya", "CSE", 88)
student_list.append(students[4])

print("\nAfter Adding New Student:")


for roll_no, details in students.items():
    print("Roll No:", roll_no, "| Name:", details[0],
          "| Branch:", details[1], "| Marks:", details[2])


# Delete student with roll number 2
del students[2]
student_list.remove(student2)

print("\nAfter Deleting Roll No. 2:")


for roll_no, details in students.items():
    print("Roll No:", roll_no, "| Name:", details[0],
          "| Branch:", details[1], "| Marks:", details[2])


# Update student with roll number 3
students[3] = ("Sneha", "CSE", 95)

print("\nAfter Updating Roll No. 3:")


for roll_no, details in students.items():
    print("Roll No:", roll_no, "| Name:", details[0],
          "| Branch:", details[1], "| Marks:", details[2])