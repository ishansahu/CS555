import gedcom_parser
import datetime

file_path = 'InputFiles/Project01.ged'

# US09: Birth before death of parents
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

# US10: Marriage after 14
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