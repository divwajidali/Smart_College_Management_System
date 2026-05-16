class Authentication:
    def __init__(self):
        pass

    def signup(self, name , email, password, role):
        
        self.info = {}
        self.info.update({"Name" : name})
        self.info.update({"Email" : email})
        self.info.update({"Password" : password})
        if (role == "Admin"):
            self.info.update({"Role" : role})
            self.info = str(self.info)
            with open("E:\GitDemo\Smart_College_Management_System\Admin.py", "a") as f:
                f.write(self.info)
                print("Signup Successfully.")
                self.ad = Admin()
                self.choice = input("1. Add Student\n2. Add Teacher\n3. All Students\n4. All Teachers\n5. Lougout\nEnter choice :")
                
                if (self.choice == "1"):
                    id = input("Enter Student ID :")
                    nme = input("Enter Student Name :")
                    age = input("Enter Student Age :")
                    emal = input("Enter Student Email :")
                    phone = input("Enter Student Phone :")
                    course = input("Enter Student Course :")
                    self.ad.add_student(id,nme, age, emal, phone, course)

                elif (self.choice == "2"):
                    id = input("Enter Teacher ID :")
                    nme = input("Enter Teacher Name :")
                    subject = input("Enter Subject :")
                    salary = input("Enter Salary :")
                    self.ad.add_teacher(id, nme, subject, salary)

                elif (self.choice == "3"):
                    self.ad.all_students()

                elif (self.choice == "4"):
                    self.ad.all_teachers()

                elif (self.choice == "5"):
                    print("Lougout Successfully.")
                    print("Exit!")

                else:
                    print("You entered an invalid option.")


        elif (role == "Teacher"):
            self.info.update({"Role" : role})
            self.info = str(self.info)
            with open("E:\GitDemo\Smart_College_Management_System\Teacher.py", "a") as f:
                f.write(self.info)
                print("Signup Successfully.")
                self.choice = input("1. Add Marks\n2.View Students\n3. Lougout\nEnter Choice :")
                self.teach = Teacher(self.choice)

        elif (role == "Student"):
            self.info.update({"Role" : role})
            self.info = str(self.info)
            with open("E:\GitDemo\Smart_College_Management_System\Student.py", "a") as f:
                f.write(self.info)
                print("Signup Successfully.")
                self.choice = input("1. View Profile\n2. View Attendance\n3. View Marks\n4. Logout\nEnter Choice :")
                self.stu = Student(self.choice)

    def login(self, email, password, role):
        

        if (role == "Admin"):
            with open("E:\GitDemo\Smart_College_Management_System\Admin.py", "r") as f:
                self.data = f.read()
                if email in self.data:
                    if password in self.data:
                        print("Login Successfully.")
                        self.ad = Admin()
                        self.choice = input("1. Add Student\n2. Add Teacher\n3. All Students\n4. All Teachers\n5. Lougout\nEnter choice :")
                        
                        if (self.choice == "1"):
                            id = input("Enter Student ID :")
                            name = input("Enter Student Name :")
                            age = input("Enter Student Age :")
                            emal = input("Enter Student Email :")
                            phone = input("Enter Student Phone :")
                            course = input("Enter Student Course :")
                            self.ad.add_student(id,name, age, emal, phone, course)

                        elif (self.choice == "2"):
                            id = input("Enter Teacher ID :")
                            name = input("Enter Teacher Name :")
                            subject = input("Enter Subject :")
                            salary = input("Enter Salary :")
                            self.ad.add_teacher(id, name, subject, salary)

                        elif (self.choice == "3"):
                            self.ad.all_students()

                        elif (self.choice == "4"):
                            self.ad.all_teachers()

                        elif (self.choice == "5"):
                            print("Lougout Successfully.")
                            print("Exit!")

                        else:
                            print("You entered an invalid option.")
                    
                    else:
                        print("Invalid user name or password.")
                else:
                    print("Invalid user name or password.")

        elif (role == "Teacher"):
            with open("E:\GitDemo\Smart_College_Management_System\Teacher.py", "r") as f:
                self.data = f.read()
                if email in self.data:
                    if password in self.data:
                        print("Login Successfully.")
                        self.choice = input("1. Add Marks\n2.View Students\n3. Lougout\nEnter Choice :")
                        self.teach = Teacher(self.choice)
                    else:
                        print("Invalid user name or password.")
                else:
                    print("Invalid user name or password.")

        elif (role == "Student"):
            with open("E:\GitDemo\Smart_College_Management_System\Student.py", "r") as f:
                self.data = f.read()
                if email in self.data:
                    if password in self.data:
                        print("Login Successfully.")
                        self.choice = input("1. View Profile\n2. View Attendance\n3. View Marks\n4. Logout\nEnter Choice :")
                        self.stu = Student(self.choice)
                    else:
                        print("Invalid user name or password.")
                else:
                    print("Invalid user name or password.")

import json
class Admin(Authentication):
    def __init__(self):
        pass

    def add_student(self, ID, name, age, email, phone, course ):
        self.std = {
            "ID" : ID,
            "Name" : name,
            "Age" : age,
            "Email" : email,
            "Phone no" : phone,
            "Course" : course
        }

        with open("E:\GitDemo\Smart_College_Management_System\Student.json", "a") as f:
            json.dump(self.std, f, indent=4)
            

    
    def add_teacher(self, ID, name, subject, salary):
        self.teacher = {
            "ID" : ID,
            "Name" : name,
            "Subject" : subject,
            "Salary" : salary
        }
        with open("E:\GitDemo\Smart_College_Management_System\Teacher.json", "a") as f:
            json.dump(self.teacher, f, indent=4)

    def all_students (self):
        with open("E:\GitDemo\Smart_College_Management_System\Student.json", "r") as f:
            self.data = json.load(f)
            print(self.data)

    def all_teachers(self):
        with open("E:\GitDemo\Smart_College_Management_System\Teacher.json", "r") as f:
            self.data = json.load(f)
            print(self.data)            
        

             
        

class Teacher(Authentication):
    def __init__(self,choice):
        self.choice = choice

class Student(Authentication):
    def __init__(self, choice):
        self.choice = choice
        

c1 = Authentication()
while True:
    choice = input("1. Singup\n2. Login\n3. Exit\nEnter Choice :")

    if (choice == "1"):
    
   
        name = input("Enter Name :")
        try :
            name = name.title()

        except ValueError:
            pass
    
        while True:
            email = input("Enter Email :")
            if (email.endswith("@gmail.com")):
            
                break
            else:
                print("You email is incorret.\nPlease enter email again.")
    
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
                    print("You enter invalid role.\nPlease enter role again.")
            except ValueError:
                print("You enter invalid role.\nPlease enter role again.")


        c1.signup(name, email, password, role)
        
        
        break



    elif (choice == "2"):

        email = input("Enter Email :")
        password = input("Enter Password :")
        role = input("Enter Role :")
        try:
            role = role.title()
        except ValueError:
            pass
     
        c1.login(email, password, role)
        break

    elif (choice == "3"):
        print("Exit!")
        break

    else:
        print("You entered an invalid option.\nPlease enter valid option.")
    