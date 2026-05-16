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
            with open("E:\GitDemo\Smart_College_Management_System\Admin.txt", "a") as f:
                f.write(self.info)
                print("Signup Successfully.")
                self.ad = Admin()

        elif (role == "Teacher"):
            self.info.update({"Role" : role})
            self.info = str(self.info)
            with open("E:\GitDemo\Smart_College_Management_System\Teacher.txt", "a") as f:
                f.write(self.info)
                print("Signup Successfully.")
                self.teach = Teacher()

        elif (role == "Student"):
            self.info.update({"Role" : role})
            self.info = str(self.info)
            with open("E:\GitDemo\Smart_College_Management_System\Student.txt", "a") as f:
                f.write(self.info)
                print("Signup Successfully.")
                self.stu = Student()

    def login(self, email, password, role):
        

        if (role == "Admin"):
            with open("E:\GitDemo\Smart_College_Management_System\Admin.txt", "r") as f:
                self.data = f.read()
                if email in self.data:
                    if password in self.data:
                        print("Login Successfully.")
                        self.ad = Admin()
                    else:
                        print("Invalid user name or password.")
                else:
                    print("Invalid user name or password.")

        elif (role == "Teacher"):
            with open("E:\GitDemo\Smart_College_Management_System\Teacher.txt", "r") as f:
                self.data = f.read()
                if email in self.data:
                    if password in self.data:
                        print("Login Successfully.")
                        self.teach = Teacher()
                    else:
                        print("Invalid user name or password.")
                else:
                    print("Invalid user name or password.")

        elif (role == "Student"):
            with open("Smart_College_Management_System/Student.txt", "r") as f:
                self.data = f.read()
                if email in self.data:
                    if password in self.data:
                        print("Login Successfully.")
                        self.stu = Student()
                    else:
                        print("Invalid user name or password.")
                else:
                    print("Invalid user name or password.")


class Admin(Authentication):
    def __init__(self):
        print("Admin Dashboard")

class Teacher(Authentication):
    def __init__(self):
        print("Teacher Dashboard")

class Student(Authentication):
    def __init__(self):
        pass

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
    