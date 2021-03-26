import gedcom_parser
import sprint2
import unittest
import datetime

# Unit test for UserStory5
# Author: Gireesh Singh Thakurathi
class UserStory5_AutoTest(unittest.TestCase):

    def test1(self):
        individualErrors = sprint2.UserStory5()

        for person in individualErrors:
            print("UserStory5: ERROR ENCOUNTERED: " + person.id + " Name " + person.name + " Death DAY "+ str(person.death) + " should not be before Marriage Date " + str(person.marriage))

        self.assertTrue(len(individualErrors) == 0, "All marriages occur before deaths.")

# Unit test for UserStory7
# Author: Gireesh Singh Thakurathi
class UserStory7_AutoTest(unittest.TestCase):

    def test1(self):
        deathError, individualErrors = sprint2.US07()
        t = datetime.datetime.today()
        today = datetime.date(t.year, t.month, t.day)

        for person in deathError:
            print("UserStory7: ERROR ENCOUNTERED: " + person.id + " Name " + person.name + " death "+ str(person.death) + " should not be greater than 150 years after birth: " + str(person.birthday))

        for person in individualErrors:
            print("UserStory7: ERROR ENCOUNTERED: " + person.id + " Name " + person.name + " birth day "+ str(person.birthday) + " should be less than 150 years from today: "+ today)

        self.assertTrue(len(deathError) == 0 and len(individualErrors) == 0, "All deaths occur less than 150 years after birth and current date is also less than 150 years after all birth")


if __name__ == '__main__':
    gedcom_parser.getOutput('InputFiles/Project01.ged')
    print("")
    unittest.main()