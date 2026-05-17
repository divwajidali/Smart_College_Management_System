import json
def validate_email():
    while True:
            email = input("Enter Email : ")
            if ("@" in email and "." in email and email.endswith(".com")):
                try:
                    with open("User.json", "r") as f :
                        data = json.load(f)

                except FileNotFoundError:
                    data = []

                exist = False
                for user in data :
                    if user["Email"] == email :
                        exist = True
                        print("Email already exist.\nPlease Enter another email.")
                        break

                if exist:
                    continue

                return email


            else:
                print("Invalid Email.\nPlease enter again.")

def check_id(filname, role):
    while True:
        id = input(f"Enter {role} ID :")

        try :
            with open(filname, "r") as f :
                data = json.load(f)

        except FileNotFoundError:
            data = []

        exist = False

        for user in data:
            if user["ID"] == id :
                exist = True
                print("ID already exist.\nTry with different ID.")
                break

        if exist :
            continue

                    
        return id
    


class User:
    def __init__(self):
        pass

    def signup(self, name , email, password, role):
        
        self.info = {
            "Name" : name,
            "Email" : email,
            "Password" : password,
            "Role" : role
        }
        
        try:
            with open("User.json", "r") as f :
                self.data = json.load(f)

        except FileNotFoundError:
            self.data = []

        self.data.append(self.info)
        with open("User.json", "w") as f :
            json.dump(self.data, f, indent=4)


        print("Signup Successfully.")
        self.email = email
        if (role == "Admin"):
            
            self.ad = Admin()
            self.ad.admin_menu()


        elif (role == "Teacher"):
            
            self.teac = Teacher()
            self.teac.teacher_menu()

        elif (role == "Student"):
            
                
            self.std = Student(self.email)
            
            self.std.student_menu()        


    def login(self, email, password):
        self.email = email
        try:
            with open("User.json", "r") as f :
                self.data = json.load(f)
                found = False
                for user in self.data:
                    if user["Email"] == email :
                        if user["Password"] == password :
                            found = True
                            print("Login Successfully.")
                            if user["Role"] == "Admin" :
            
                                self.ad = Admin()
                                self.ad.admin_menu()


                            elif user["Role"] == "Teacher":
            
                                self.teac = Teacher()
                                self.teac.teacher_menu()


                            elif user["Role"] == "Student":
            
                
                                self.std = Student(self.email)
                                self.std.student_menu()
                            break


                    
                if not found :
                    print("Invalid Email or password.")
        except FileNotFoundError:
            print("Invalid Email or password.")

class Admin(User):
    def __init__(self):
        pass


    def admin_menu(self):
        while True:
            self.choice = input("1. Add Student\n2. Add Teacher\n3. All Students\n4. All Teachers\n5. Logout\nEnter choice :")
                
            if (self.choice == "1"):
                id = check_id("Student.json", "Student")             
                name = input("Enter Student Name :")
                age = input("Enter Student Age :")
                email = validate_email()
                
                phone = input("Enter Student Phone :")
                course = input("Enter Student Course :")
                self.add_student(id,name, age, email, phone, course)

            elif (self.choice == "2"):
                id = check_id("Teacher.json", "Teacher")
                name = input("Enter Teacher Name :")
                subject = input("Enter Subject :")
                salary = input("Enter Salary :")
                self.add_teacher(id, name, subject, salary)

            elif (self.choice == "3"):
                self.all_students()

            elif (self.choice == "4"):
                self.all_teachers()

            elif (self.choice == "5"):
                print("Logout Successfully.")
                print("Exit!")
                break
            else:
                print("You entered an invalid option.")

    def add_student(self, ID, name, age, email, phone, course ):
        self.std = {
            "ID" : ID,
            "Name" : name,
            "Age" : age,
            "Email" : email,
            "Phone no" : phone,
            "Course" : course
        }

        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)

        except FileNotFoundError:
            self.data = []

        self.data.append(self.std)    
        with open("Student.json", "w") as f:
            json.dump(self.data, f, indent=4)
            

    
    def add_teacher(self, ID, name, subject, salary):
        self.teacher = {
            "ID" : ID,
            "Name" : name,
            "Subject" : subject,
            "Salary" : salary
        }

        try:
            with open("Teacher.json", "r") as f :
                self.data = json.load(f)

        except FileNotFoundError:
            self.data = []

        self.data.append(self.teacher)    
        with open("Teacher.json", "w") as f:
            json.dump(self.data, f, indent=4)

    def all_students (self):
        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)

        except FileNotFoundError:
            self.data = "No student found."

        print("-" * 120)

        print(f"{'ID' :<10}{'Name' :<15}{'Age' :<10}{'Email' :<30}{'Phone' :<30}{'Course' :<15}{'Marks' :<10}")

        print("-" * 120)
        for student in self.data :
            print(f"{student['ID'] :<10}{student['Name'] :<15}{student['Age'] :<10}{student['Email'] :<30}{student['Phone no'] :<30}{student['Course'] :<15}{student.get('Marks', 'N/A') :<10}")
        print("-" * 120)

    def all_teachers(self):
        try:
            with open("Teacher.json", "r") as f:
                self.data = json.load(f)
            
        except FileNotFoundError:
            self.data = "No teacher found."
        print("-" * 60)

        print(f"{'ID' :<10}{'Name' :<15}{'Subject' :<20}{'Salary' :<15}")

        print("-" * 60)
        for teacher in self.data :
            print(f"{teacher['ID'] :<10}{teacher['Name'] :<15}{teacher['Subject'] :<20}{teacher['Salary'] :<15}")
        print("-" * 60)
        

             
    

class Teacher(User):
    def __init__(self):
        pass

    def teacher_menu(self):

        while True :
            self.choice = input("1. Add Marks\n2.View Students\n3. Logout\nEnter Choice :")

            if (self.choice == "1"):
                ID = input("Enter ID :")
                marks = input("Enter Marks :")
                self.marks(ID, marks)

            elif (self.choice == "2"):
                self.view_students()

            elif (self.choice == "3"):
                print("Logout Successfully.\nExit!")
                break

            else:
                print("You entered invalid option.")

    def marks(self, ID, marks):
        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)
                found = False
                for i in self.data:
                    if i["ID"] == ID :
                        i["Marks"] = marks
                        found = True
                        break

                if found:
                    with open("Student.json", "w") as f :
                        json.dump(self.data, f, indent=4)
                    print("Marks added successfully.")

                else:
                    print("Student not found.")


        except FileNotFoundError:
            print("Student not found.")

    def view_students (self):
        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)

        except FileNotFoundError:
            self.data = "No student found."

        print("-" * 120)

        print(f"{'ID' :<10}{'Name' :<15}{'Age' :<10}{'Email' :<30}{'Phone' :<30}{'Course' :<15}{'Marks' :<10}")

        print("-" * 120)
        for student in self.data :
            print(f"{student['ID'] :<10}{student['Name'] :<15}{student['Age'] :<10}{student['Email'] :<30}{student['Phone no'] :<30}{student['Course'] :<15}{student.get('Marks', 'N/A') :<10}")
        print("-" * 120)

class Student(User):
    def __init__(self, email):
        self.email = email
    
    def student_menu(self):
        while True:

            self.choice = input("1. View Profile\n2. View Marks\n3. Logout\nEnter Choice :")
            if (self.choice == "1"):
                self.view_profile()

            elif(self.choice == "2"):
                self.view_marks()

            elif (self.choice == "3"):
                print("Logout Successfully.\nExit!")
                break

            else:
                print("You entered invalid option.")

    def view_profile(self):
        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)
                found = False
                for student in self.data:
                    if student["Email"] == self.email :
                        
                        print("-" * 120)

                        print(f"{'ID' :<10}{'Name' :<15}{'Age' :<10}{'Email' :<30}{'Phone' :<30}{'Course' :<15}{'Marks' :<10}")

                        print("-" * 120)
        
                        print(f"{student['ID'] :<10}{student['Name'] :<15}{student['Age'] :<10}{student['Email'] :<30}{student['Phone no'] :<30}{student['Course'] :<15}{student.get('Marks', 'N/A') :<10}")
                        print("-" * 120)
                        found = True
                        break

                if not found :
                    print("Profile not found.")

        except FileNotFoundError:
            print("Profile not found.")
        
    def view_marks(self):
        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)
                found = False
                for student in self.data:
                    if student["Email"] == self.email :
                        print(f"Marks : {student.get('Marks', 'N/A')}")
                        found = True
                        break

                if not found :
                    print("Profile not found.")

        except FileNotFoundError:
            print("Profile not found.")

c1 = User()
while True:
    choice = input("1. Signup\n2. Login\n3. Exit\nEnter Choice :")

    if (choice == "1"):
    
   
        name = input("Enter Name :")
        try :
            name = name.title()

        except ValueError:
            pass
    
        email = validate_email()
    
        while True:
            password = input("Enter Password :")
            if (len(password) < 8):
                print("Your password is less than 8 character.\nPlease enter password again.")
    

            else:
            
                break

        while True:
            role = input("Enter Role :")
            try:
                role = role.title()

                if (role == "Admin"):
                
                    break

                elif (role == "Teacher"):
                
                    break

                elif(role == "Student"):
                
                    break

                else:
                    print("You entered invalid role.\nPlease enter role again.")
            except ValueError:
                print("You entered invalid role.\nPlease enter role again.")


        c1.signup(name, email, password, role)
        
        
        



    elif (choice == "2"):

        email = input("Enter Email :")
        password = input("Enter Password :")
     
        c1.login(email, password)
        

    elif (choice == "3"):
        print("Exit!")
        break

    else:
        print("You entered an invalid option.\nPlease enter valid option.")
    

