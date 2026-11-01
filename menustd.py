#Menu-driven student information
students={}
def add_student():
    roll=input("Enter Roll Number:")
    name=input("Enter Name:")
    dept=input("Enter Department:")
    students[roll]={"Name":name,"Department":dept}
    print("Student added succesfully")
def view_students():
    if not students:
        print("No students record found")
        return
    print("\n---Students Records---")
    for roll,data in students.items():
        print("Roll NO:",roll,"|Name:",data["Name"],"|Department:",data["Department"])
def search_student():
    roll=input("Enter roll number to search:")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found")
def delete_student():
    roll=input("Enter Roll No to search:")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found")
while True:
    print("\n1.Add Student")
    print("\n2.View Students")
    print("\n3.Search Student")
    print("\n4.Delete Student")
    print("\n5.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
      
