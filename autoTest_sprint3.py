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

if __name__ == '__main__':
    gedcom_parser.getOutput('InputFiles/Project01.ged')
    print("")
    unittest.main()