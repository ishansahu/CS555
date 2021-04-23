import gedcom_parser
import datetime

file_path = 'InputFiles/Project01.ged'

# UserStory9: Birth before death of parents
# Child should be born before death of mother and before 9 months after death of father
# Author: Gireesh Singh Thakurathi
def UserStory9():
    peopleList, famList = gedcom_parser.parse(file_path)

    childerror = []

    for fam in famList:
        if len(fam.children) > 0:
            if fam.husbandId!='NA':
                husb = gedcom_parser.getPerson(fam.husbandId, peopleList)
                for child in fam.children:
                    c = gedcom_parser.getPerson(child, peopleList)
                    if husb.death !='NA':
                        newYear = ( husb.death.month + 9 ) // 12
                        newMonth = (husb.death.month + 9 ) % 12
                        if newMonth == 0:
                            newMonth = 12
                        limit = datetime.date(husb.death.year + newYear, newMonth, husb.death.day)
                        if c.birthday > limit:
                            childerror.append(c)
            if fam.wifeId != 'NA':
                wife = gedcom_parser.getPerson(fam.wifeId, peopleList)
                for child in fam.children:
                    c = gedcom_parser.getPerson(child, peopleList)
                    if wife.death !='NA':
                        if c.birthday > wife.death:
                            childerror.append(c)

    return childerror

# UserStory10: Marriage after 14
# Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
# Author: Gireesh Singh Thakurathi
def UserStory10():
    listPeople, listFam = gedcom_parser.parse(file_path)

    marriageFailed_list =[]

    for fam in listFam:
        if fam.husbandId!='NA':
            husb= gedcom_parser.getPerson(fam.husbandId, listPeople)
            limit = husb.birthday.year + 14
            if fam.married != 'NA' and fam.married.year < limit:
                marriageFailed_list.append(husb)
        if fam.wifeId!='NA':
            wife = gedcom_parser.getPerson(fam.wifeId, listPeople)
            limit = wife.birthday.year + 14
            if fam.married != 'NA' and fam.married.year < limit:
                marriageFailed_list.append(wife)

    return marriageFailed_list


# UserStory8 Birth before marriage of parents
# Children should be born after marriage of parents and no more than 9 months after their divorce.
# Author: Ishan Sahu

def UserStory08():
    marriageFailed_list = []
    divorceFailed_list = []
    peopleList, famList = gedcom_parser.parse(file_path)
    curr_datetime = datetime.datetime.today()
    today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
    for fam in famList:
        if len(fam.children) > 0:
            if fam.divorced != "NA":
                newYear = ( fam.divorced.month + 9 ) // 12
                newMonth = (fam.divorced.month + 9 ) % 12
                if newMonth == 0:
                    newMonth = 12
                limit = datetime.date(fam.divorced.year + newYear, newMonth, fam.divorced.day)
                for child in fam.children:
                    c = gedcom_parser.getPerson(child, peopleList)
                    if c.birthday > limit:
                        divorceFailed_list.append([c,fam.divorced,fam.id])
            elif fam.married != "NA":
                for child in fam.children:
                    c = gedcom_parser.getPerson(child, peopleList)
                    if c.birthday < fam.married:
                        marriageFailed_list.append([c,fam.married, fam.id])

    return marriageFailed_list, divorceFailed_list




# UserStory11 No bigamy
# Individual should not be married to 2 or more people at the same time.
# Author: Ishan Sahu

def UserStory11():
    peopleList, famList = gedcom_parser.parse(file_path)
    individualFailed_list = []
    for fam in famList:
        if fam.husbandId != 'NA':
            husb = gedcom_parser.getPerson(fam.husbandId, peopleList)
            if fam.married != 'NA':
                husb.marriageList.append(fam.married)
            if fam.divorced != 'NA':
                husb.divorceList.append(fam.divorced)
        if fam.wifeId != 'NA':
            wife = gedcom_parser.getPerson(fam.wifeId, peopleList)
            if fam.married != 'NA':
                wife.marriageList.append(fam.married)
            if fam.divorced != 'NA':
                wife.divorceList.append(fam.divorced)
    for person in peopleList:
        if len(person.marriageList) == 0 and len(person.divorceList) == 0:
            continue
        else:
            if len(person.marriageList) > 1 and len(person.divorceList) == 0:
                individualFailed_list.append(person)
            elif len(person.marriageList) > 1:
                marr = person.marriageList
                div = person.divorceList
                marr.sort()
                div.sort()
                for i in range(1, len(marr)):
                    for j in range(0, len(div)):
                        if marr[i] < div[j]:
                            individualFailed_list.append(person)
                            break
    return individualFailed_list
