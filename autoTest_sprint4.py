import gedcom_parser
import sprint2
import unittest
import datetime


import sprint4

# Unittest for UserStory12
# Author: Ishan Sahu
class UserStory12_AutoTest(unittest.TestCase):
    def test_US12_individuals(self):
        individualFailed_list = sprint4.UserStory12()
        for person in individualFailed_list:
            if person[1].gender == "M":
                print("ERROR: INDIVIDUAL: UserStory12: " + person[1].id + " Name " + person[
                    1].name + " is more than 80 years older than the child " + person[
                          0].id + ": Father's birthday " + str(person[1].birthday) + ", Child's birthday " + str(
                    person[0].birthday))
            else:
                print("ERROR: INDIVIDUAL: UserStory12: " + person[1].id + " Name " + person[
                    1].name + " is more than 60 years older than the child " + person[
                          0].id + ": Mother's birthday " + str(person[1].birthday) + ", Child's birthday " + str(
                    person[0].birthday))
        self.assertTrue(len(individualFailed_list) == 0, "USer Story 12: Completed")


# Unit test for UserStory15
# Author: Ishan Sahu
class UserStory15_AutoTest(unittest.TestCase):
    def test_US15_individuals(self):
        familyFailed_list = sprint4.UserStory15()
        for family in familyFailed_list:
            print("ERROR: FAMILY: UserStory15: " + family.id + " has more than 15 siblings")
        self.assertTrue(len(familyFailed_list) == 0, "UserStory15: Completed")

# Unit test for UserStory13
# Author: Gireesh Singh Thakurathi
class UserStory13_AutoTest(unittest.TestCase):

    def test1(self):
        sibling_Failed_list = sprint4.UserStory13()

        for sib in sibling_Failed_list:
            print("UserStory13: ERROR ENCOUNTERED: "+ sib[0].name + " Birthday " +  str(sib[0].birthday) + " is within incorrect spacing with " + sib[1].name + " Birthday " + str(sib[1].birthday))

        self.assertTrue(len(sibling_Failed_list) == 0, " All siblings birthday are correctly spaced!")

# Unit test for UserStory14
# Author: Gireesh Singh Thakurathi
class UserStory14_AutoTest(unittest.TestCase):

    def test1(self):
        sibling_Failed_list = sprint4.UserStory14()

        for fam in sibling_Failed_list:
            print("UserStory14: ERROR ENCOUNTERED: "+ fam.id + " has 5 or more children with the same birthday")

        self.assertTrue(len(sibling_Failed_list) == 0 , " Number of children with same birthday is less than 5")

# Unit test for UserStory16
# Author: Gireesh Singh Thakurathi
class UserStory16_AutoTest(unittest.TestCase):
    def test_US16_individuals(self):
        Error = sprint4.UserStory16()

        for family in Error:
            print("UserStory16: ERROR ENCOUNTERED: " + family.id + " has last name mismatch in males")

        self.assertTrue(len(Error) == 0, "All male members of every family have the same last name")

if __name__ == '__main__':
    gedcom_parser.getOutput('InputFiles/Project01.ged')
    print("")
    unittest.main()