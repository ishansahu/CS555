import gedcom_parser
import datetime

file_path = 'InputFiles/Project01.ged'

# US05: Marriage Before Death
# Marriage should occur before death of an individual
# Author: Gireesh Singh Thakurathi
def UserStory5():
    peopleList, famList = gedcom_parser.parse(file_path)
    individualFailed_list=[]
    for fam in famList:
        if fam.husbandId != 'NA':
            h = gedcom_parser.getPerson(fam.husbandId, peopleList)
            husb = h.createDeepCopy(h)
            if fam.married != 'NA' and husb.alive == False and husb.death < fam.married:
                husb.marriage = fam.married
                individualFailed_list.append(husb)
        if fam.wifeId != 'NA':
            w = gedcom_parser.getPerson(fam.wifeId, peopleList)
            wife = w.createDeepCopy(w)
            if fam.married != 'NA'  and wife.alive==False and wife.death < fam.married:
                wife.marriage = fam.married
                individualFailed_list.append(wife)
    return individualFailed_list


# UserStory6 Divorce before death
# Divorce should occur before death of any spouses, and divorce can only occur after marriage
# Author: Ishan Sahu
def UserStory6():
    peopleList, famList = gedcom_parser.parse(file_path)
    individualFailed_list=[]
    for fam in famList:
        if fam.husbandId != 'NA':
            husb = gedcom_parser.getPerson(fam.husbandId, peopleList)
            if fam.divorced != 'NA' and not husb.alive and husb.death < fam.divorced:
                husb.divorce = fam.divorced
                individualFailed_list.append(husb)
        if fam.wifeId != 'NA':
            wife = gedcom_parser.getPerson(fam.wifeId, peopleList)
            if fam.divorced != 'NA' and not wife.alive and wife.death < fam.divorced:
                wife.divorce = fam.divorced
                individualFailed_list.append(wife)
    return individualFailed_list


# UserStory7 less than 150 years old
# Birth date should not be more than 150 years from today. In case of Death, age should not be greater than 150 years.
# Author: Gireesh Thakurathi and Ishan Sahu
def UserStory7():
    peopleList, famList = gedcom_parser.parse(file_path)
    curr_datetime = datetime.datetime.today()
    today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
    deathFailed_list, peopleFailed_list = [],[]
    for person in peopleList:
        if not person.alive :
            limit = person.birthday.year + 150
            if person.death.year > limit:
                deathFailed_list.append(person)
        if today.year > person.birthday.year + 150 and person.alive :
            peopleFailed_list.append(person)
    return deathFailed_list, peopleFailed_list

