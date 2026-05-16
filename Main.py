class Authentication:
    def __init__(self):
        pass

    def signup(self, name , email, password, role):
        self.name = name
        self.email = email
        self.role = role
        self.password = password
        
        

c1 = Authentication()
choice = input("1. Singup\n2. Login\nEnter Choice :")

if (choice == "1"):
    info = {}
   
    name = input("Enter Name :")
    info.update({"Name" : name})
    while True:
        email = input("Enter Email :")
        if (email.endswith("@gmail.com")):
            info.update({"Email" : email})
            break
        else:
            print("You email is incorret.\nPlease enter email again.")
    
    while True:
        password = input("Enter Password :")
        if (len(password) < 8):
            print("Your password is less than 8 character.\nPlease enter password again.")
    

        else:
            info.update({"Password" : password})
            break

    while True:
        role = input("Enter Role :")
        try:
            role = role.title()

            if (role == "Admin"):
                info.update({"Role" : role})
                info = str(info)
                with open("Admin.txt", "a") as f:
                    f.write(info)
                break

            elif (role == "Teacher"):
                info.update({"Role" : role})
                info = str(info)
                with open("Teacher.txt", "a") as f:
                    f.write(info)
                break

            elif (role == "Student"):
                info.update({"Role" : role})
                info = str(info)
                with open("Student.txt", "a") as f:
                    f.write(info)
                break

            else:
                print("You enter invalid role.\nPlease enter role again.")
        except ValueError:
            print("You enter invalid role.\nPlease enter role again.")


    c1.signup(name, email, password, role)
    print("Signup Successfully.")