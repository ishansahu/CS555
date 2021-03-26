import gedcom_parser

file_path = 'InputFiles/Project01.ged'

# US05: Marriage Before Death
# Marriage should occur before death of an individual
# Author: Gireesh Singh Thakurathi
def UserStory5():
    file_ = 'gedcomTests/main_test.ged'
    peopleList, famList = gedcom_parser.parse(file_)
    individualFailed_list=[]
    for fam in famList:
        if fam.husbandId != 'NA':
            h = gedcom_parser.findPerson(fam.husbandId, peopleList)
            husb = h.createDeepCopy(h)
            if fam.married != 'NA' and husb.alive == False and husb.death < fam.married:
                husb.marriage = fam.married
                individualFailed_list.append(husb)
        if fam.wifeId != 'NA':
            w = gedcom_parser.findPerson(fam.wifeId, peopleList)
            wife = w.createDeepCopy(w)
            if fam.married != 'NA'  and wife.alive==False and wife.death < fam.married:
                wife.marriage = fam.married
                individualFailed_list.append(wife)
    return individualFailed_list