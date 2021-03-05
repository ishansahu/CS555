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
        if len(individualErrors) > 0:
            for person in individualErrors:
                if person.birthday == 'NA':
                    print("UserStory1: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " does not have a birthday")
        self.assertTrue(len(individualErrors) == 0, "All individuals have BIRTH DATES.")

    def test_2(self):
        individualErrors, famErrors = sprint1.UserStory1()
        curr_datetime = datetime.datetime.today()
        today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
        if len(individualErrors)>0:
            for person in individualErrors:
                if person.birthday > today:
                    print("UserStory1: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " Birthday "+ str(person.birthday)+" should be before today")
        self.assertTrue(len(individualErrors) == 0, "All individual BIRTH DATES occur before today.")

    def test_3(self):
        individualErrors, famErrors = sprint1.UserStory1()
        curr_datetime = datetime.datetime.today()
        today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
        if len(individualErrors)>0:
            for person in individualErrors:
                if person.death != 'NA' and person.death > today:
                    print("UserStory1: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " Death day "+ str(person.death)+" should be before today")
        self.assertTrue(len(individualErrors) == 0, "All individual DEATH DATES occur before today.")

    def test_4(self):
        individualErrors, famErrors = sprint1.UserStory1()
        curr_datetime = datetime.datetime.today()
        today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
        if len(famErrors) > 0:
            for fam in famErrors:
                if fam.married != 'NA' and fam.married > today:
                    print("UserStory1: ENCOUNTERED ERROR: " + fam.id + " Marriage Date "+ str(fam.married) +" should be before today")
        self.assertTrue(len(famErrors) == 0, "All MARRIAGE DATES occur before today.")

    def test_5(self):
        individualErrors, famErrors = sprint1.UserStory1()
        curr_datetime = datetime.datetime.today()
        today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
        if len(famErrors)>0:
            for fam in famErrors:
                if fam.divorced != 'NA' and fam.divorced > today:
                    print("UserStory1: ENCOUNTERED ERROR: " + fam.id + " Divorce Date "+ str(fam.divorced) +" should be before today")
        self.assertTrue(len(famErrors) == 0, "All DIVORCE DATES occur before today.")


# Unit test for UserStory2
# Author: Gireesh Singh Thakurathi
class UserStory2_AutoTest(unittest.TestCase):
    def test1(self):
        individualErrors = sprint1.UserStory2()
        if len(individualErrors) > 0:
            for person in individualErrors:
                print("UserStory2: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " Marriage date " + str(
                    person.marriage) + " should be after Birthday " + str(person.birthday))
        self.assertTrue(len(individualErrors) == 0, "All BIRTHDAYS occur before MARRIAGE DATE.")


# Unit test for UserStory3
# Author: Ishan Sahu
class UserStory3_AutoTest(unittest.TestCase):
    def test1(self):
        individualErrors = sprint1.UserStory3()
        flag = True
        if len(individualErrors) > 0:
            for person in individualErrors:
                if person.alive and person.death != "NA":
                    flag = False
                    print("UserStory3: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + "is alive and "
                                                                                                   "death date is not "
                                                                                                   "null ")
        self.assertTrue(flag, "No alive person's death date is set.")

    def test2(self):
        individualErrors = sprint1.UserStory3()
        flag = True
        if len(individualErrors) > 0:
            for person in individualErrors:
                if not person.alive and person.death == "NA":
                    flag = False
                    print("UserStory3: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + "is dead and death "
                                                                                                   "date is not set.")
        self.assertTrue(flag, "All dead person's death date is set")

    def test3(self):
        individualErrors = sprint1.UserStory3()
        curr_datetime = datetime.datetime.today()
        today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
        flag = True
        if len(individualErrors) > 0:
            for person in individualErrors:
                if not person.alive and person.death > today:
                    flag = False
                    print(
                        "UserStory3: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " Death Date: " + str(
                            person.death) + " should be before today's date " + str(today))
        self.assertTrue(flag, "All dead persons death date is before today's date.")

    def test4(self):
        individualErrors = sprint1.UserStory3()
        flag = True
        if len(individualErrors) > 0:
            for person in individualErrors:
                if not person.alive and person.birthday > person.death:
                    flag = False
                    print("UserStory3: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " Death Date: " + str(
                        person.death) + " should be before Birthday " + str(person.birthday))
        self.assertTrue(flag, "All birth dates occur before death date")

    def test5(self):
        individualErrors = sprint1.UserStory3()
        flag = True
        if len(individualErrors) > 0:
            for person in individualErrors:
                if not person.birthday:
                    flag = False
                    print(
                        "UserStory3: ENCOUNTERED ERROR: " + person.id + " Name " + person.name + " birthdate is not set")
        self.assertTrue(flag, "All birth dates are set")


# Unit test for UserStory4
# Author: Ishan Sahu
class UserStory4_AutoTest(unittest.TestCase):
    def test1(self):
        famErrors = sprint1.UserStory4()
        if len(famErrors) > 0:
            for fam in famErrors:
                print("UserStroy4: ENCOUNTERED ERROR: " + fam.id + " Marriage date: " + str(
                    fam.married) + " should occur before Divorce date: " + str(fam.divorced))
        self.assertTrue(len(famErrors) == 0, "All MARRIAGE DATES occur before DIVORCE.")


if __name__ == '__main__':
    gedcom_parser.getOutput('InputFiles/Project01.ged')
    print("")
    unittest.main()
