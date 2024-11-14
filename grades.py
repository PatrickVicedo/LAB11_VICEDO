grade_list = []
subjects = 0  
print("Please enter 'done' to exit")


while True:
    grade_input = input("Enter Your Grade: ")

    if grade_input.lower() == "done":
        print("Exiting the loop.")
        break

    
    if grade_input.replace('.', '', 1).isdigit():
        grade_numbers = float(grade_input)
        if 40 <= grade_numbers <= 100:
            grade_list.append(grade_numbers)
            if grade_numbers >= 75:
                subjects += 1
        else:
            print("Incorrect Data. Please enter a grade between 40 and 100.")
    else:
        print("Invalid input. Please enter a numeric grade or 'done' to exit.")

if grade_list:
    total_grades = sum(grade_list)
    avg_grade = total_grades / len(grade_list)
    

    pass_percentage = (subjects / len(grade_list)) * 100

    print(f"Average Grade  {avg_grade:.2f}")
    print(f"Number of passed subjects: {subjects}")
    print(f"Percentage Subjects Passed: {pass_percentage:.2f}%")
    print("Grades Entered:", grade_list)
else:
    print("No valid grades were entered.")
