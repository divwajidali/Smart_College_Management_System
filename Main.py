import json
class User:
    def __init__(self):
        pass

    def signup(self, name , email, password, role):
        
        self.info = {}
        self.info.update({"Name" : name})
        self.info.update({"Email" : email})
        self.info.update({"Password" : password})
        self.info.update({"Role" : role})
        try:
            with open("User.json", "r") as f :
                self.data = json.load(f)

        except:
            self.data = []

        self.data.append(self.info)
        with open("User.json", "w") as f :
            json.dump(self.data, f, indent=4)


        print("Signup Successfully.")

        if (role == "Admin"):
            
            self.ad = Admin()
            self.choice = input("1. Add Student\n2. Add Teacher\n3. All Students\n4. All Teachers\n5. Logout\nEnter choice :")
                
            if (self.choice == "1"):
                while True:
                    id = input("Enter Student ID :")

                    try :
                        with open("Student.json", "r") as f :
                            data = json.load(f)

                    except :
                        data = []

                    exist = False

                    for user in data:
                        if user["ID"] == id :
                            exist = True
                            print("ID already exist.\nTry with different ID.")
                            break

                    if exist :
                        continue

                    
                    break
                             
                nme = input("Enter Student Name :")
                age = input("Enter Student Age :")
                while True:
                    emal = input("Enter Email : ")

                    if ("@" in emal and "." in emal and emal.endswith(".com")):
                        try:
                            with open("User.json", "r") as f :
                                data = json.load(f)

                        except:
                            data = []

                        exist = False
                        for user in data :
                            if user["Email"] == emal :
                                exist = True
                                print("Email already exist.\nPlease Enter another email.")
                                break

                        if exist :
                            continue

                        break

                    else:
                        print("Invalid Email.\nPlease enter again.")
                phone = input("Enter Student Phone :")
                course = input("Enter Student Course :")
                self.ad.add_student(id,nme, age, emal, phone, course)

            elif (self.choice == "2"):
                
                while True:
                    id = input("Enter Teacher ID :")

                    try :
                        with open("Teacher.json", "r") as f :
                            data = json.load(f)

                    except :
                        data = []

                    exist = False

                    for user in data:
                        if user["ID"] == id :
                            exist = True
                            print("ID already exist.\nTry with different ID.")
                            break

                    if exist :
                        continue

                    
                    break
                nme = input("Enter Teacher Name :")
                subject = input("Enter Subject :")
                salary = input("Enter Salary :")
                self.ad.add_teacher(id, nme, subject, salary)

            elif (self.choice == "3"):
                self.ad.all_students()

            elif (self.choice == "4"):
                self.ad.all_teachers()

            elif (self.choice == "5"):
                print("Logout Successfully.")
                print("Exit!")

            else:
                print("You entered an invalid option.")


        elif (role == "Teacher"):
            
            self.teac = Teacher()
            self.choice = input("1. Add Marks\n2.View Students\n3. Logout\nEnter Choice :")

            if (self.choice == "1"):
                ID = input("Enter ID :")
                marks = input("Enter Marks :")
                self.teac.marks(ID, marks)

            elif (self.choice == "2"):
                self.teac.view_students()

            elif (self.choice == "3"):
                print("Logout Successfully.\nExit!")

            else:
                print("You entered invalid option.")


        elif (role == "Student"):
            
                
            self.std = Student()
            self.choice = input("1. View Profile\n2. View Marks\n3. Logout\nEnter Choice :")
            if (self.choice == "1"):
                ID = input("Enter ID :")
                self.std.view_profile(ID)

            elif(self.choice == "2"):
                ID = input("Enter ID :")
                self.std.view_marks(ID)

            elif (self.choice == "3"):
                print("Lougout Successfully.\nExit!")

            else:
                print("You entered invalid option.")


    def login(self, email, password):
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
                                self.choice = input("1. Add Student\n2. Add Teacher\n3. All Students\n4. All Teachers\n5. Logout\nEnter choice :")
                
                                if (self.choice == "1"):
                                
                                    while True:
                                        id = input("Enter Student ID :")

                                        try :
                                            with open("Student.json", "r") as f :
                                                data = json.load(f)

                                        except :
                                            data = []

                                        exist = False

                                        for user in data:
                                            if user["ID"] == id :
                                                exist = True
                                                print("ID already exist.\nTry with different ID.")
                                                break

                                        if exist :
                                            continue

                                        
                                        break
                                    name = input("Enter Student Name :")
                                    age = input("Enter Student Age :")
                                    while True:
                                        emal = input("Enter Email : ")

                                        if ("@" in emal and "." in emal and emal.endswith(".com")):
                                            try:
                                                with open("User.json", "r") as f :
                                                    data = json.load(f)

                                            except:
                                                data = []

                                            exist = False
                                            for user in data :
                                                if user["Email"] == emal :
                                                    exist = True
                                                    print("Email already exist.\nPlease Enter another email.")
                                                    break

                                            if exist:
                                                continue

                                            break

                                        else:
                                            print("Invalid Email.\nPlease enter again.")
                                    phone = input("Enter Student Phone :")
                                    course = input("Enter Student Course :")
                                    self.ad.add_student(id,name, age, emal, phone, course)

                                elif (self.choice == "2"):
                                    while True:
                                        id = input("Enter Teacher ID :")

                                        try :
                                            with open("Teacher.json", "r") as f :
                                                data = json.load(f)

                                        except :
                                            data = []

                                        exist = False

                                        for user in data:
                                            if user["ID"] == id :
                                                exist = True
                                                print("ID already exist.\nTry with different ID.")
                                                break

                                        if exist :
                                            continue

                                        
                                        break
                                    name = input("Enter Teacher Name :")
                                    subject = input("Enter Subject :")
                                    salary = input("Enter Salary :")
                                    self.ad.add_teacher(id, name, subject, salary)

                                elif (self.choice == "3"):
                                    self.ad.all_students()

                                elif (self.choice == "4"):
                                    self.ad.all_teachers()

                                elif (self.choice == "5"):
                                    print("Logout Successfully.")
                                    print("Exit!")

                                else:
                                    print("You entered an invalid option.")


                            elif user["Role"] == "Teacher":
            
                                self.teac = Teacher()
                                self.choice = input("1. Add Marks\n2.View Students\n3. Logout\nEnter Choice :")

                                if (self.choice == "1"):
                                    ID = input("Enter ID :")
                                    marks = input("Enter Marks :")
                                    self.teac.marks(ID, marks)

                                elif (self.choice == "2"):
                                    self.teac.view_students()

                                elif (self.choice == "3"):
                                    print("Logout Successfully.\nExit!")

                                else:
                                    print("You entered invalid option.")


                            elif user["Role"] == "Student":
            
                
                                self.std = Student()
                                self.choice = input("1. View Profile\n2. View Marks\n3. Logout\nEnter Choice :")
                                if (self.choice == "1"):
                                    ID = input("Enter ID :")
                                    self.std.view_profile(ID)

                                elif(self.choice == "2"):
                                    ID = input("Enter ID :")
                                    self.std.view_marks(ID)

                                elif (self.choice == "3"):
                                    print("Lougout Successfully.\nExit!")

                                else:
                                    print("You entered invalid option.")


                    
                if not found :
                    print("Invalid Email or password.")
        except:
            print("Invalid Email or password.")

class Admin(User):
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

        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)

        except:
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

        except:
            self.data = []

        self.data.append(self.teacher)    
        with open("Teacher.json", "w") as f:
            json.dump(self.data, f, indent=4)

    def all_students (self):
        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)

        except:
            self.data = "No student found."
        print(self.data)

    def all_teachers(self):
        try:
            with open("Teacher.json", "r") as f:
                self.data = json.load(f)
            
        except:
            self.data = "No teacher found."
        print(self.data)            
        

             
    

class Teacher(User):
    def __init__(self):
        pass

    
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
                    print("Marks added successfully.")

                else:
                    print("Student not found.")


        except:
            print("Student not found.")

        with open("Student.json", "w") as f:
            json.dump(self.data, f , indent=4)

    def view_students (self):
        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)

        except:
            self.data = "No student found."
        print(self.data)

class Student(User):
    def __init__(self):
        pass

    def view_profile(self, ID):
        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)
                found = False
                for student in self.data:
                    if student["ID"] == ID :
                        print(student)
                        found = True
                        break

                if not found :
                    print("Student not found.")

        except:
            print("Student not found.")
        
    def view_marks(self, ID):
        try:
            with open("Student.json", "r") as f:
                self.data = json.load(f)
                found = False
                for student in self.data:
                    if student["ID"] == ID :
                        print(f"Marks : {student['Marks']}")
                        found = True
                        break

                if not found :
                    print("Student not found.")

        except:
            print("Student not found.")

c1 = User()
while True:
    choice = input("1. Signup\n2. Login\n3. Exit\nEnter Choice :")

    if (choice == "1"):
    
   
        name = input("Enter Name :")
        try :
            name = name.title()

        except ValueError:
            pass
    
        while True:
            email = input("Enter Email : ")

            if ("@" in email and "." in email and email.endswith(".com")):
                try:
                    with open("User.json", "r") as f :
                        data = json.load(f)

                except:
                    data = []

                exist = False
                for user in data :
                    if user["Email"] == email :
                        exist = True
                        print("Email already exist.\nPlease Enter another email.")
                        break

                if exist:
                    continue

                break


            else:
                print("Invalid Email.\nPlease enter again.")
    
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
        
        
        break



    elif (choice == "2"):

        email = input("Enter Email :")
        password = input("Enter Password :")
     
        c1.login(email, password)
        break

    elif (choice == "3"):
        print("Exit!")
        break

    else:
        print("You entered an invalid option.\nPlease enter valid option.")
    