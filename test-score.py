# Program 4.17 Test score averages

# Get the number of students.
num_students = int(input("How many students do you have?: "))

# Get the number of test scores per student.
num_test_scores = int(input("How many test scores per student?: "))

print()

# Determine each student's averege test score.
for student in range(num_students) :
    # Initilaize an accumulator for test scores.
    total = 0.0
    # Get the student's test scores.
    print("student number", student + 1)
    print("---------------------")

    for test_num in range(num_test_scores) :
        print("Test number", test_num + 1, end='')
        score = float(input(": "))
        # Add the score to the accumulator.
        total = total + score

    # Calculate the averge test score for this student.
    average = total / num_test_scores

    # Display the average.
    print("The average for student number", student + 1, "is:", format(average, '.2f'))
    
    print() 