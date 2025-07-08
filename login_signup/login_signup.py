import hashlib
class Student:
    def __init__(self):
        self.name = "Ram"
        self.age = 20
        self.roll_no = 793
        self.user_name = "root"
        self.pass_word = self.hash_password("1234")
        self.login_count = 0
        self.user = []
        


    def signup(self):
        
        username = input("Enter a username: ")
        try:
            user_password = input("Enter a strong password: ")
            hashed_user_password = self.hash_password(user_password)
        except Exception as e:
            print("Error while creating password!",e)    

        try:
            self.user.append({
                "username":username,
                "password":hashed_user_password
            })
            print("signup successfully")
            print(self.user)
        except Exception as e:
            print("signup error")
        



    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    

    def printInfo(self):
        print("Student Details: ")
        print("Name:", self.name)
        print("Age: ", self.age)
        print("Roll No: ", self.roll_no)



    def login(self):
        
        for i in range(3):

            self.username = input("Enter Username: ")
            try:
                self.password = input("Enter the password: ")
                hashed_pass = self.hash_password(self.password)
            except ValueError:
                print("Password must be a number.")
                self.login_count +=1
                continue
        
            for u in self.user:
                if u["username"] == self.username and u["password"] == hashed_pass:
                    print("You now logged in..👍")
                    self.printInfo()
                    return
            else:
                print("Invalid username or password ❌")
                self.login_count += 1
                print(f"Attempts left: {2-self.login_count}")
        print("Too many attempts. Access denied.")

s1 = Student()
print("Welcome to the Student dashboard!")
while True:
    print("1. Signup  2. Login  3.Exit")
    choice = int(input("choose any option.."))
    match choice:
        case 1: 
            print("Signup progress..")
            s1.signup()
        case 2: 
            print("Login progress..")
            s1.login()
        case 3: 
            print("Exiting..")
            break
        case _: print("Invalid choice")
