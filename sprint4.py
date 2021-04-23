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

