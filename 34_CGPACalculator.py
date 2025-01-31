# Dictionary to store grade values
grade_points = {
    "A+": 4.00, "A": 3.75, "B+": 3.50, "B": 3.00,
    "C": 2.50, "D": 1.75, "F": 0.00
}

def calculate_cgpa():
    num_subjects = int(input("Enter the number of subjects: "))

    total_credit_hours = 0
    total_weighted_gpa = 0

    for i in range(num_subjects):
        credit_hours = float(input(f"Enter credit hours for subject {i+1}: "))
        grade = input(f"Enter letter grade for subject {i+1} (A+, A, B+, B, C, D, F): ").strip().upper()

        if grade not in grade_points:
            print("Invalid grade entered. Please enter a valid grade.")
            return

        total_credit_hours += credit_hours
        total_weighted_gpa += credit_hours * grade_points[grade]

    if total_credit_hours == 0:
        print("Total credit hours cannot be zero.")
    else:
        cgpa = total_weighted_gpa / total_credit_hours
        print(f"\nYour final CGPA is: {cgpa:.2f}")

# Run the function
calculate_cgpa()
