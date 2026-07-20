# Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good Job! You can do even better! 😊"
    elif marks >= 60:
        return "D", "Keep Practicing! Success is near! 💪"
    else:
        return "F", "Don't give up! Keep learning and try again! 📚"


# Get student name
student_name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100.")

    except ValueError:
        print("❌ Please enter a valid number.")

grade, message = calculate_grade(marks)

print("\n" + "=" * 35)
print(f"📊 RESULT FOR {student_name.upper()}")
print("=" * 35)
print(f"Marks : {marks}/100")
print(f"Grade : {grade}")
print(f"Message : {message}")