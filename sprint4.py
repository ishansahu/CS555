import gedcom_parser
import datetime

file_path = 'InputFiles/Project01.ged'

# UserStory12 Parents not too old
# Mother should be less than 60 years older than her children and father should be less than 80 years older
# Author: Ishan Sahu

def UserStory12():
    listPeople, listFam = gedcom_parser.parse(file_path)
    individualFailed_list=[]
    for fam in listFam:
        if len(fam.children) > 0:
            if fam.husbandId != 'NA':
                husb = gedcom_parser.getPerson(fam.husbandId, listPeople)
            for child in fam.children:
                c = gedcom_parser.getPerson(child, listPeople)
                limit = husb.birthday.year + 80
                if c.birthday.year > limit:
                    individualFailed_list.append([c, husb])
            if fam.wifeId != 'NA':
                wife = gedcom_parser.getPerson(fam.wifeId, listPeople)
            for child in fam.children:
                c = gedcom_parser.getPerson(child, listPeople)
                limit = wife.birthday.year + 60
                if c.birthday.year > limit:
                    individualFailed_list.append([c, wife])
    return individualFailed_list


# UserStory15 Fewer than 15 siblings
# There should be fewer than 15 siblings in a family
# Author: Ishan Sahu

def UserStory15():
    file_ = 'gedcomTests/main_test.ged'
    listPeople, listFam = gedcom_parser.parse(file_)

    familyFailed_list=[]
    for fam in listFam:
        if len(fam.children) >= 15:
            familyFailed_list.append(fam)

    return familyFailed_list

# UserStory13 Sibling spacing
# Birth dates of siblings should be more than 8 months apart or less than 2 days apart
# Author: Gireesh Singh Thakurathi

def UserStory13():
    peopleList, famList = gedcom_parser.parse(file_path)

    errorList = []

    for fam in famList:
        if len(fam.children) > 0:
            for i in range(len(fam.children)):
                c1 = gedcom_parser.getPerson(fam.children[i], peopleList)
                newYear = ( c1.birthday.month + 8 ) // 12
                newMonth = (c1.birthday.month + 8 ) % 12
                if newMonth == 0:
                    newMonth = 12
                limit1 = datetime.date(c1.birthday.year + newYear, newMonth, c1.birthday.day)
                limit2 = c1.birthday + datetime.timedelta(days=2)
                for j in range(len(fam.children)):
                    if i != j:
                        c2 = gedcom_parser.getPerson(fam.children[j], peopleList)
                        if c2.birthday < limit1 and c2.birthday > limit2:
                            errorList.append([c1,c2])
    return errorList

# UserStory14 Multiple Births <= 5
# No more than five siblings should be born at the same time
# Author: Gireesh Singh Thakurathi

def UserStory14():
    peopleList, famList = gedcom_parser.parse(file_path)

    siblingCountError = []

    count = 0
    for fam in famList:
        if len(fam.children) >= 5:
            for i in range(len(fam.children)):
                c1 = gedcom_parser.findPerson(fam.children[i], peopleList)
                for j in range(len(fam.children)):
                    if i != j:
                        c2 = gedcom_parser.findPerson(fam.children[j], peopleList)
                        if c1.birthday == c2.birthday:
                            count += 1
                if count >= 5:
                    siblingCountError.append(fam)
                    break;
                else:
                    count = 0
                    continue;
    return siblingCountError

# UserStory16 Male last names
# All male members of a family should have the same last name
# Author: Gireesh Singh Thakurathi

def UserStory16():
    peopleList, famList = gedcom_parser.parse(file_path)

    lastnameerror=[]
    for fam in famList:
        if fam.husbandId!='NA':
            husb = gedcom_parser.getPerson(fam.husbandId, peopleList)
            list_name_husb=husb.name.split()
            if len(fam.children)>0:
                for child in fam.children:
                    c = gedcom_parser.getPerson(child, peopleList)
                    if c.gender=="M":
                        list_child_name=c.name.split()
                        if list_name_husb[-1] != list_child_name[-1]:
                            lastnameerror.append(fam)
    return lastnameerror