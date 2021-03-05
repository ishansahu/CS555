#   Course: CS-555
#   Team 8

from prettytable import PrettyTable
from datetime import date

class family(object):
    def __init__(self, arg):
        self.id = arg
        self.married = "NA"
        self.divorced = "NA"
        self.husbandId = "NA"
        self.husbandName = "NA"
        self.wifeId = "NA"
        self.wifeName = "NA"
        self.children = []
    def setMarriageDate(self, date):
        self.married = date
    def setDivorceDate(self, divorced):
        self.divorced = divorced
    def setHusband(self, id_, husbandName):
        self.husbandId = id_
        self.husbandName = husbandName
    def setWife(self, id_, wifeName):
        self.wifeId = id_
        self.wifeName = wifeName
    def addChildren(self, child):
        self.children.append(child)

class person(object):
    def __init__(self, arg):
        self.id = arg
        self.name = ""
        self.gender = ""
        self.birthday = ""
        self.alive = True
        self.age = 0
        self.death = "NA"
        self.children = []
        self.spouse = "NA"
        self.countID= ""
    def setName(self, name):
        self.name = name
    def setGender(self, gender):
        self.gender = gender
    def setBirthday(self, birthday):
        self.birthday = birthday
    def setAlive(self, alive):
        self.alive = alive
    def setAge(self, age):
        self.age = age
    def setDeath(self, death):
        self.death = death
    def addChildren(self, children):
        self.children.append(children)
    def setSpouse(self, spouse):
        self.spouse = spouse
    def createDeepCopy(self, p):
        copyp = person(p.id)
        copyp.name = p.name
        copyp.gender = p.gender
        copyp.birthday = p.birthday
        copyp.alive = p.alive
        copyp.age = p.age
        copyp.death = p.death
        copyp.children = p.children
        copyp.spouse = p.spouse
        copyp.countID = p.countID
        return copyp

def getFamily(id_, familyList):
    ans = ""
    for fam in familyList:
        if fam.id == id_:
            return fam
    return ans

def getParents(id_, familyList):
    ans = ""
    for fam in familyList:
        if id_ in fam.children:
            return fam
    return ans

def getPerson(id_, personList):
    ans = ""
    for p in personList:
        if p.id == id_:
            return p
    return ans

def getPersonByCountId(id_, personList):
    ans = ""
    for p in personList:
        if p.countID == id_:
            return p
    return ans

def areSiblings(family1, family2, familyList):
    if family1.id == family2.id:
        return False
    f1 = getParents(family1.wifeId, familyList)
    f2 = getParents(family2.wifeId, familyList)
    f3 = getParents(family1.husbandId, familyList)
    f4 = getParents(family2.husbandId, familyList)

    if f3:
        if f4:
            if f3.id == f4.id:
                return True
        elif f2:
            if f3.id == f2.id:
                return True
    elif f1:
        if f4:
            if f1.id == f4.id:
                return True
        elif f2:
            if f1.id == f2.id:
                return True

    return False

def toMonth(month):
    allMonth = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
    return allMonth[month]

# Adding Display functionality using PrettyTable
def printOutput(personList, familyList):
    families = PrettyTable(["ID","Married","Divorce","Husband ID","Husband Name","Wife ID","Wife Name","Children"])
    for p in familyList:
        children = 'NA' if len(p.children) == 0 else '{'+str(p.children).strip('[]')+'}'
        families.add_row([p.id, p.married, p.divorced, p.husbandId, p.husbandName, p.wifeId, p.wifeName, children])
    persons = PrettyTable(["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"])
    for p in personList:
        children = 'NA' if p.children == 'NA' else '{'+str(p.children).strip('[]')+'}'
        persons.add_row([p.id, p.name, p.gender, p.birthday, str(p.age), str(p.alive), p.death, children, p.spouse])
    print('Individuals')
    print(persons)
    print("Families")
    print(families)

def getOutput(file_path):
    peopleList, familyList = parse(file_path)
    printOutput(peopleList, familyList)

def parse(file_path):
    level = tag = argument = "Not Found"
    tag_map = { '0' : ['HEAD','NOTE','TRLR'],
                '1' : ['BIRT','CHIL','DIV','HUSB','WIFE','MARR','NAME','SEX','DEAT','FAMC','FAMS'],
                '2' : ['DATE']}
    peopleList = []
    familyList = []
    countP = 0
    try:
        with open(file_path) as ged_file:
            birth = False
            death = False
            married = False
            divorced = False
            currentTag = ""
            for line in ged_file:
                line = line.strip()
                args = line.split(" ")
                number_of_args = len(args)
                if number_of_args == 3 and args[0] == '0' and args[2] in {'INDI','FAM'}:
                    level, tag, argument = args
                    valid_tags = 'Y'
                    if argument == 'INDI':
                        countP+=1
                        currentId = tag.strip('@')
                        newP = person(currentId)
                        newP.countID = countP
                        peopleList.append(newP)
                        currentTag = 'INDI'
                    elif argument == 'FAM':
                        currentId = tag.strip('@')
                        newFam = family(currentId)
                        familyList.append(newFam)
                        currentTag = 'FAM'
                elif number_of_args >= 2:
                    level, tag = args[0],args[1]
                    argument = " ".join(args[2:])
                    if level in tag_map and tag in tag_map[level]:
                        valid_tags ='Y'
                        if currentTag == 'INDI':
                            if birth == True and tag == 'DATE':
                                birthday = date(int(args[4]), toMonth(args[3]), int(args[2]))
                                p = getPersonByCountId(countP, peopleList)
                                p.setBirthday(birthday)
                                age = int(args[4])
                                p.setAge(2020-age)
                                birth = False
                            elif death == True and tag == 'DATE':
                                deathday = date(int(args[4]), toMonth(args[3]), int(args[2]))
                                p = getPersonByCountId(countP, peopleList)
                                p.setDeath(deathday)
                                p.setAlive(False)
                                death = False
                            elif tag == 'NAME':
                                name = " ".join(args[2:])
                                p = getPersonByCountId(countP, peopleList)
                                p.setName(name)
                            elif tag == 'SEX':
                                gender = args[2]
                                p = getPersonByCountId(countP, peopleList)
                                p.setGender(gender)
                            elif tag == 'BIRT':
                                birth = True
                                continue;
                            elif tag == 'DEAT':
                                death = True
                                continue;
                        elif currentTag == 'FAM':
                            if married == True and tag == 'DATE':
                                fam = getFamily(currentId, familyList)
                                marriedDate = date(int(args[4]), toMonth(args[3]), int(args[2]))
                                fam.setMarriageDate(marriedDate)
                                married = False
                            elif divorced == True and tag == 'DATE':
                                fam = getFamily(currentId, familyList)
                                divDate = date(int(args[4]), toMonth(args[3]), int(args[2]))
                                fam.setDivorceDate(divDate)
                                divorced = False
                            elif tag == 'MARR':
                                married = True
                                continue;
                            elif tag == 'DIV':
                                divorced = True
                                continue;
                            elif tag == 'HUSB':
                                husbandId = args[2].strip('@')
                                fam = getFamily(currentId, familyList)
                                husband = getPerson(husbandId, peopleList)
                                fam.setHusband(husbandId, husband.name)
                            elif tag == 'WIFE':
                                wifeId = args[2].strip('@')
                                fam = getFamily(currentId, familyList)
                                wife = getPerson(wifeId, peopleList)
                                fam.setWife(wifeId, wife.name)
                            elif tag == 'CHIL':
                                childId = args[2].strip('@')
                                fam = getFamily(currentId, familyList)
                                fam.addChildren(childId)
                    else:
                        valid_tags = 'N'
                else:
                    valid_tags ='N'
                    level, tag, argument =args
                # print("<--{}|{}|{}|{}".format(level, tag, valid_tags, argument))
            for fam in familyList:
                if fam.husbandId != 'NA':
                    husband = getPerson(fam.husbandId, peopleList)
                    if fam.wifeId != 'NA':
                        husband.setSpouse(fam.wifeId)
                    if len(fam.children) > 0:
                        for child in fam.children:
                            husband.addChildren(child)
                if fam.wifeId != 'NA':
                    wife = getPerson(fam.wifeId, peopleList)
                    if fam.husbandId != 'NA':
                        wife.setSpouse(fam.husbandId)
                    if len(fam.children) > 0:
                        for child in fam.children:
                            wife.addChildren(child)
            printOutput(peopleList, familyList)
    except:
        print("File not found or can't be accessed")
    return peopleList, familyList
    
parse('InputFiles/Project01.ged')