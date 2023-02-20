import login
import unittest


class Testing(unittest.TestCase):
    secure0 = login.Security("Aidanaedy1", "Password156", 0)
    secure1 = login.Security("Bobby", "Password1$", 10)
    secure2 = login.Security("Linda", "Password2$", 20)
    secure3 = login.Security("David", "Password3$", 30)

    #  test 1
    def test_login1(self):
        self.assertEqual(login.secure.login(), True)

    #  test 2
    def test_login2(self):
        self.assertEqual(login.secure.username, "Aidanaedy")

    #  test 3
    def test_login3(self):
        self.assertEqual(login.secure.password, "Password156")

    #  test 4
    def test_login4(self):
        self.assertEqual(login.secure.companyID , 10)

    #  test 5
    def test_login5(self):
        self.assertEqual(login.secure.login_output(), f"The username and password are validated and username "
                                                      f"has {len(login.secure.username)} characters, the "
                                                      f"password has {len(login.secure.password)} "
                                                      f"characters and the ID is number {login.secure.companyID}")

    #  test 6
    def test_login6(self):
        self.assertEqual(self.secure0.login_output(), f"The username and password are validated and username "
                                                      f"has 10 characters, the "
                                                      f"password has 11 "
                                                      f"characters and the ID is number 0")

    #  test 7
    def test_login7(self):
        self.assertEqual(self.secure0.username, "Aidanaedy1")

    #  test 8
    def test_login8(self):
        self.assertEqual(self.secure0.password, "Password156")

    #  test 9
    def test_login9(self):
        self.assertEqual(self.secure0.companyID, 0)

    #  test 10
    def test_login10(self):
        self.assertEqual(self.secure2.login() , True)

    #  test 11 "Bobby", "Password1$", 10)
    def test_login11(self):
        self.assertEqual(self.secure1.login_output(), f"The username and password are validated and username "
                                                      f"has 5 characters, the "
                                                      f"password has 10 "
                                                      f"characters and the ID is number 10")

    #  test 12
    def test_login12(self):
        self.assertEqual(self.secure1.username, "Bobby")

    #  test 13
    def test_login13(self):
        self.assertEqual(self.secure1.password, "Password1$")

    #  test 14
    def test_login14(self):
        self.assertEqual(self.secure1.companyID, 10)
