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
