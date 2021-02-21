import gedcom_parser
import sprint1
import unittest
import datetime

# Unit test for UserStory1
# Author: Gireesh Singh Thakurathi
class UserStory1_AutoTest(unittest.TestCase):
    def test_1(self):
        individualErrors, famErrors = sprint1.UserStory1()
        curr_datetime = datetime.datetime.today()
        today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
        if len(individualErrors)>0:
            for person in individualErrors:
                if person.birthday > today:
                    print("UserStory1: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " Birthday "+ str(person.birthday)+" should be before today")
                elif person.death != 'NA' and person.death > today:
                    print("UserStory1: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " Death day "+ str(person.death)+" should be before today")
        self.assertTrue(len(individualErrors) == 0, "All individual BIRTH and DEATH DATES occur before today.")

    def test_2(self):
        individualErrors, famErrors = sprint1.UserStory1()
        curr_datetime = datetime.datetime.today()
        today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
        if len(famErrors)>0:
            for fam in famErrors:
                if fam.married != 'NA' and fam.married > today:
                    print("UserStory1: ENCOUNTERED ERROR: " + fam.id + " Marriage Date "+ str(fam.married) +" should be before today")
                elif fam.divorced != 'NA' and fam.divorced > today:
                    print("UserStory1: ENCOUNTERED ERROR: " + fam.id + " Divorce Date "+ str(fam.divorced) +" should be before today")
        self.assertTrue(len(famErrors) == 0, "All MARRIAGE and DIVORCE DATES occur before today.")

# Unit test for UserStory2
# Author: Gireesh Singh Thakurathi
class UserStory2_AutoTest(unittest.TestCase):
    def test1(self):
        individualErrors = sprint1.UserStory2()
        if len(individualErrors)>0:
            for person in individualErrors:
                print("UserStory2: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " Marriage date "+ str(person.marriage) + " should be after Birthday " + str(person.birthday))
        self.assertTrue(len(individualErrors) == 0, "All BIRTHDAYS occur before MARRIAGE DATE.")

if __name__ == '__main__':
    gedcom_parser.outputTable('InputFiles/sprint1.ged')
    print("")
    unittest.main()
