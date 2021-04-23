import gedcom_parser
import sprint3
import unittest

# Unit test for UserStory9
# Author: Gireesh Singh Thakurathi
class UserStory9_AutoTest(unittest.TestCase):
    def test1(self):
        individualFailed_list = sprint3.UserStory9()
        for person in individualFailed_list:
            print("UserStory9: ERROR ENCOUNTERED: " + person.id + " Name " + person.name + " is born on " + str(person.birthday)+ " which is after death of mother or after 9 months after death of father")

        self.assertTrue(len(individualFailed_list) == 0, "Everyone was born before the death of their parents")

# Unit test for UserStory10
# Author: Gireesh Singh Thakurathi
class UserStory10_AutoTest(unittest.TestCase):
    def test1(self):
        marriageFailed_List = sprint3.UserStory10()

        for person in marriageFailed_List:
            print("UserStory10: ERROR ENCOUNTERED: " + person.id + " Name " + person.name + " is less than 14 years of age before marriage on  "+str(person.marriage))

        self.assertTrue(len(marriageFailed_List) == 0, "All individuals were married when they were older than 14 years")


# Unit test for UserStory 08
# Author: Ishan Sahu
class UserStory08_AutoTest(unittest.TestCase):
    def test1(self):
        marriageFailed_list, divorceFailed_list = sprint3.UserStory08()
        for person in marriageFailed_list:
            print("UserStory 08: ERROR: ENCOUNTERED: " + person[0].id + " Name " + person[0].name + " born BEFORE marriage date of FAMILY: "+ person[2] + " : " + str(person[1]))

        for person in divorceFailed_list:
            print("UserStory 08: ERROR: ENCOUNTERED: " + person[0].id + " Name " + person[0].name + " born 9 months AFTER divorce date of FAMILY: " + person[2] + " : " + str(person[1]))

        self.assertTrue(len(marriageFailed_list) == 0 and len(divorceFailed_list) == 0, "All BIRTHS are correct and occur correctly as per parents Marriage/Divorce dates!")

# Unit test for UserStory 11
# Author: Ishan Sahu
class UserStory11_AutoTest(unittest.TestCase):
    def test1(self):
        individualFailed_list = sprint3.UserStory11()
        for person in individualFailed_list:
            print("ERROR: INDIVIDUAL: US11: " + person.id + " Name " + person.name + " BIGAMY error, married to more than 1 person at the same time")
        self.assertTrue(len(individualFailed_list) == 0, "All people are married to 1 person at a given time.")




if __name__ == '__main__':
    gedcom_parser.getOutput('InputFiles/Project01.ged')
    print("")
    unittest.main()