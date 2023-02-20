""" login(string username, string password, int companyID)
The returned Boolean value is set to true if users are validated and to false if they are not.
The above method resides in a class called Security which is the class under test (CUT).
"""


class Security:
    def __init__(self, username="Johndoe", password="false", company_id=0):
        self.companyID = company_id
        self.username = username
        self.password = password

        if self.username == "Johndoe" and self.password == "false":
            self.username = input("Please enter your Username: ")
            self.password = input("Please enter your Password: ")
            self.companyID = int(input("Please enter your Company ID: "))
        else:
            pass

    def login(self):
        if self.username == "" \
                and not len(self.username) > 3 \
                and not self.username.isalpha()\
                and any(char.isdigit() for char in self.username) \
                and self.password == "" \
                and not any(char.isdigit() for char in self.password) \
                and not len(self.password) > 8 \
                and not 1 <= self.companyID < 100 \
                and not type(self.companyID) == int :
            return False
        else:
            return True

    def login_output(self):
        if self.login():
            return f"The username and password are validated and username has {len(self.username)} characters, " \
                   f"the password has {len(self.password)} characters and the ID is number {self.companyID}"
        else:
            return "The username and password are not Validated, please try again"

    def is_user_valid(self):
        # create a stub for unit testing. These will go into a database later
        if self.username == "Bobby" and self.password == "Password1$" and self.companyID == 10:
            return f"The username and password are validated but bobby is here "
        elif self.username == "Linda" and self.password == "Password2$" and self.companyID == 20:
            return f"The username and password are validated but Penny is here "
        elif self.username == "David" and self.password == "Password3$" and self.companyID == 30:
            return f"The username and password are validated but Rose is here "
        else:
            return "No agents have been detected!"


secure = Security("Aidanaedy", "Password156", 10)
secure_bobby = Security("Bobby", "Password1$", 10)
print(secure.username, "= User Name ,", secure.password, "= Password ,", secure.companyID, "= ID number")
print(secure.is_user_valid())
print(secure.login_output())
print(secure_bobby.username, "= User Name ,", secure_bobby.password, "= Password ,", secure_bobby.companyID, "= ID number")
print(secure_bobby.is_user_valid())
print(secure_bobby.login_output())
