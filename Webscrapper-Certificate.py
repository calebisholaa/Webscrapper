import requests
from bs4 import BeautifulSoup, NavigableString
import re
import csv

class GraduateProgram:
        def __init__(self, programName="", coordinatorName="", coordinatorPhone="",  coordinatorEmail="", deliveryMethod=""):
                self.programName = programName
                self.coordinatorName = coordinatorName
                self.coordinatorPhone = coordinatorPhone
                self.coordinatorEmail  = coordinatorEmail
                self.deliveryMethod = deliveryMethod



graduateProgramList =[]

URL = "https://www.etsu.edu/gradschool/certificate-programs.php"


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

programsResult = soup.find('main')
int;i=1
for program in programsResult.find_all('details'):

      #programName - for example Audiology -Au.D, Biomedical Science -Ph.D
    programName = program.find('summary').get_text().strip()

    

    if program.find(string="Coordinator") != None:

        coordinatorInfo = program.find(string="Coordinator").findNext('ul').get_text()

        phoneIndex = re.search(r'Phone:', coordinatorInfo)
        emailIndex = re.search(r'Email:', coordinatorInfo)
        
        if phoneIndex != None:
            if emailIndex != None:
        
                coordinatorName = coordinatorInfo[0 : phoneIndex.start()].strip()
                coordinatorPhone = coordinatorInfo[phoneIndex.start() + 7 :emailIndex.start()].strip()
                coordinatorEmail = coordinatorInfo[emailIndex.start() + 7:].strip()

                deliveryMethod = program.find(string="Location/Delivery Method").findNext('ul').contents[0].nextSibling.get_text()

                gradProgram = GraduateProgram(programName, coordinatorName, coordinatorPhone, coordinatorEmail,deliveryMethod)
                if gradProgram not in graduateProgramList:
                                graduateProgramList.append(gradProgram)

        elif phoneIndex == None:
                
                coordinatorName = coordinatorInfo[0 : emailIndex.start()].strip()
                coordinatorPhone = "Null"
                coordinatorEmail = coordinatorInfo[emailIndex.start() + 7:].strip()

                deliveryMethod = program.find(string="Location/Delivery Method").findNext('ul').contents[0].nextSibling.get_text()

                gradProgram = GraduateProgram(programName, coordinatorName, coordinatorPhone, coordinatorEmail,deliveryMethod)
                if gradProgram not in graduateProgramList:
                                graduateProgramList.append(gradProgram)
        elif emailIndex == None:
                
                coordinatorName = coordinatorInfo[0 : emailIndex.start()].strip()
                coordinatorPhone = coordinatorInfo[phoneIndex.start() + 7 :emailIndex.start()].strip()
                coordinatorEmail = "Null"
                deliveryMethod = program.find(string="Location/Delivery Method").findNext('ul').contents[0].nextSibling.get_text()

                gradProgram = GraduateProgram(programName, coordinatorName, coordinatorPhone, coordinatorEmail,deliveryMethod)
                if gradProgram not in graduateProgramList:
                                graduateProgramList.append(gradProgram)

    elif program.find(string="Coordinator ") != None:
       
        coordinatorInfo = program.find(string="Coordinator ").findNext('ul').get_text()

        phoneIndex = re.search(r'Phone:', coordinatorInfo)
        emailIndex = re.search(r'Email:', coordinatorInfo)

        if phoneIndex != None:
            if emailIndex != None:
        
                coordinatorName = coordinatorInfo[0 : phoneIndex.start()].strip()
                coordinatorPhone = coordinatorInfo[phoneIndex.start() + 7 :emailIndex.start()].strip()
                coordinatorEmail = coordinatorInfo[emailIndex.start() + 7:].strip()

                deliveryMethod = program.find(string="Location/Delivery Method").findNext('ul').contents[0].nextSibling.get_text()

                gradProgram = GraduateProgram(programName, coordinatorName, coordinatorPhone, coordinatorEmail,deliveryMethod)
                if gradProgram not in graduateProgramList:
                                graduateProgramList.append(gradProgram)

        elif phoneIndex == None:
                
                coordinatorName = coordinatorInfo[0 : emailIndex.start()].strip()
                coordinatorPhone = "Null"
                coordinatorEmail = coordinatorInfo[emailIndex.start() + 7:].strip()

                deliveryMethod = program.find(string="Location/Delivery Method").findNext('ul').contents[0].nextSibling.get_text()

                gradProgram = GraduateProgram(programName, coordinatorName, coordinatorPhone, coordinatorEmail,deliveryMethod)
                if gradProgram not in graduateProgramList:
                                graduateProgramList.append(gradProgram)
        elif emailIndex == None:
                
                coordinatorName = coordinatorInfo[0 : emailIndex.start()].strip()
                coordinatorPhone = coordinatorInfo[phoneIndex.start() + 7 :emailIndex.start()].strip()
                coordinatorEmail = "Null"
                deliveryMethod = program.find(string="Location/Delivery Method").findNext('ul').contents[0].nextSibling.get_text()

                gradProgram = GraduateProgram(programName, coordinatorName, coordinatorPhone, coordinatorEmail,deliveryMethod)
                if gradProgram not in graduateProgramList:
                                graduateProgramList.append(gradProgram)


      
with open('Programs_Coordinators_Certificate.csv', mode='w') as csv_file:
	writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
	
	writer.writerow(["Program Name - Type ; Concentration", "Coordinator's Name", "Coordinator's Phone Number", "Coordinator's Email","Delivery Method"])
	
	for study in graduateProgramList:
		writer.writerow([study.programName,study.coordinatorName, study.coordinatorPhone, study.coordinatorEmail, study.deliveryMethod])




with open('All_Programs_Coordinators.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
	
        
	
        for study in graduateProgramList:
	        writer.writerow(["Certificate Programs" ,study.programName,study.coordinatorName, study.coordinatorPhone, study.coordinatorEmail, study.deliveryMethod])