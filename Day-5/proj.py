# Student Management System

students = []  # List to store student details

def add_student():
    """Function to add a new student."""
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    subjects = input("Enter subjects (comma-separated): ").split(",")
    
    student = {
        "name": name,
        "age": age,
        "subjects": tuple(subjects)  # Storing subjects as a tuple
    }
    
    students.append(student)
    print(f" ✅ Student {name} added successfully!\n")

def display_students():
    """Function to display all students."""
    if not students:
        print("No students found! ❌")
        return

    print("\n📌 Student Records:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']}, Age: {student['age']}, Subjects: {student['subjects']}")

def update_student():
    """Function to update student details."""
    name = input("Enter student name to update: ")
    
    for student in students:
        if student["name"] == name:
            new_age = int(input("Enter new age: "))
            new_subjects = input("Enter new subjects (comma-separated): ").split(",")

            student["age"] = new_age
            student["subjects"] = tuple(new_subjects)
            
            print(f"✅ {name}'s record updated successfully!\n")
            return
    
    print("❌ Student not found!")

def remove_student():
    """Function to remove a student."""
    name = input("Enter student name to remove: ")
    
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print(f"🗑️  {name} removed successfully!\n")
            return
    
    print("❌ Student not found!")

# Menu loop
while True:
    print("\n📚 Student Management System")
    print("1️⃣  Add Student")
    print("2️⃣  Display Students")
    print("3️⃣  Update Student")
    print("4️⃣  Remove Student")
    print("5️⃣  Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        remove_student()
    elif choice == "5":
        print("🚀 Exiting Student Management System. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please select a valid option.")

