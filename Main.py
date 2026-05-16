class Authentication:
    def __init__(self):
        pass

    def signup(self, name , email, password, role):
        self.name = name
        self.email = email
        self.role = role
        self.password = password
        self.info = {}
        self.info.update({"Name" : name})
        self.info.update({"Email" : email})
        self.info.update({"Password" : password})
        if (role == "Admin"):
                self.info.update({"Role" : role})
                self.info = str(self.info)
                with open("E:\GitDemo\Smart_College_Management_System\Admin.txt", "a") as f:
                    f.write(self.info)

        elif (role == "Teacher"):
                self.info.update({"Role" : role})
                self.info = str(self.info)
                with open("E:\GitDemo\Smart_College_Management_System\Teacher.txt", "a") as f:
                    f.write(self.info)

        elif (role == "Student"):
                self.info.update({"Role" : role})
                self.info = str(self.info)
                with open("E:\GitDemo\Smart_College_Management_System\Student.txt", "a") as f:
                    f.write(self.info)


c1 = Authentication()
choice = input("1. Singup\n2. Login\nEnter Choice :")

if (choice == "1"):
    
   
    name = input("Enter Name :")
    
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
    print("Signup Successfully.")