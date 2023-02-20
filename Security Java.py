# This class checks for the login requirements and will also identify 3 particular individuals
class Security:
	def __init__(self, user_name="Johndoe", password="false", company_id=0):
		self.user_name = user_name
		self.password = password
		self.company_id = int(company_id)

	def login(self):
		if not self.user_name == "" \
			and len(self.user_name) > 3 \
			and self.user_name.isalpha() \
			and not any(char.isdigit() for char in self.user_name) \
			and not self.password == "" \
			and len(self.password) >= 8 \
			and not self.password.isalpha() \
			and any(char.isdigit() for char in self.password) \
			and 1 <= self.company_id < 100 \
			and type(self.company_id) == int:
			return True
		else:
			return False

	def is_user_valid(self):
		# create a stub for unit testing. These will go into a database later
		if self.user_name == "Bobby" and secure1.password == "Password1$" and secure1.company_id == 10:
			return f"The username and password are validated but bobby is here "
		if secure1.user_name == "Linda" and secure1.password == "Password2$" and secure1.company_id == 20:
			return f"The username and password are validated but Penny is here "
		if secure1.user_name == "David" and secure1.password == "Password3$" and secure1.company_id == 30:
			return f"The username and password are validated but Rose is here "
		if secure1.login():
			return f"The username and password are validated and username has {len(secure1.user_name)} characters, " \
				   f"the password has {len(secure1.password)} characters and the ID is number {secure1.company_id}"
		else:
			return "The username and password are not Validated, please try again"


secure1 = Security("Aidanaedy", "Password156", 2)
print(secure1.user_name, "= User Name ,", secure1.password, "= Password ,", secure1.company_id, "= ID number")
print(secure1.is_user_valid())


