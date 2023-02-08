import requests
from bs4 import BeautifulSoup, NavigableString
import re
class GraduateProgram:
        def __init__(self, programName="", coordinatorName="", coordinatorPhone="",  coordinatorEmail="", deliveryMethod=""):
                self.programName = programName
                self.coordinatorName = coordinatorName
                self.coordinatorPhone = coordinatorPhone
                self.coordinatorEmail  = coordinatorEmail
                self.deliveryMethod = deliveryMethod
        
       
def between(cur, end):
	string = []
	while cur and cur != end:
		if isinstance(cur, NavigableString):
			text = cur.strip()
			if len(text) and text != "Coordinators" and text != "Phone:" and text != "Email:":
				string.append(text)
		cur = cur.next_element
	
	return string


graduateProgramList =[]

URL = "https://www.etsu.edu/gradschool/masters-degrees.php"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

programsResult = soup.find('main')

for program in programsResult.find_all('details'):

        #programName - for example Audiology -Au.D, Biomedical Science -Ph.D
        programName = program.find('summary').get_text().strip()
        #print(programName)

        #If the program has only one Coordinator - this logic handles the Coordinator written with Space at the end
        if program.find(string="Coordinator ") != None:
              #Getting Coordinator Info
                coordinatorInfo = program.find(string="Coordinator ").findNext('ul').get_text()
                
     
                phoneIndex = re.search(r'Phone:', coordinatorInfo)
                emailIndex = re.search(r'Email:', coordinatorInfo)
               

                coordinatorName = coordinatorInfo[0 : phoneIndex.start()].strip()
                coordinatorPhone = coordinatorInfo[phoneIndex.start() + 7 :emailIndex.start()].strip()
                coordinatorEmail = coordinatorInfo[emailIndex.start() + 7:].strip()
               

                #Getting Program Location/Delivery Method
                deliveryMethod = program.find(string="Location/Delivery Method").findNext('ul').contents[0].nextSibling.get_text()
               # print(coordinatorName +" " + coordinatorPhone + " " + coordinatorEmail+ " "+  deliveryMethod )
                gradProgram = GraduateProgram(programName, coordinatorName, coordinatorPhone, coordinatorEmail,deliveryMethod)
                

                if gradProgram not in graduateProgramList:
                        graduateProgramList.append(gradProgram)

         #If the program has only one Coordinator - this logic handles the Coordinator written with no Space at the end
        elif program.find(string="Coordinator") != None:
              #Getting Coordinator Info
                coordinatorInfo = program.find(string="Coordinator").findNext('ul').get_text()
                
     
                phoneIndex = re.search(r'Phone:', coordinatorInfo)
                emailIndex = re.search(r'Email:', coordinatorInfo)
                inquiriesIndex = re.search(r'Inquiries', coordinatorInfo)
                formsIndex = re.search(r'Forms:', coordinatorInfo)
             
             #This logic handles a special case where the coordinator does not have a email, but forms and inqiries 
                if emailIndex == None:
                    coordinatorName = coordinatorInfo[0 : phoneIndex.start()].strip()
                    coordinatorPhone = coordinatorInfo[phoneIndex.start() + 7 :inquiriesIndex.start()].strip()
                    coordinatorInquiries = coordinatorInfo[inquiriesIndex.start() + 11 :formsIndex.start()].strip()
                    coordinatorForm = coordinatorInfo[formsIndex.start() + 7:].strip()
                    coordinatorEmail = "Inquiries: " + coordinatorInquiries +  "Form: " + coordinatorForm
                else:
                    coordinatorName = coordinatorInfo[0 : phoneIndex.start()].strip()
                    coordinatorPhone = coordinatorInfo[phoneIndex.start() + 7 :emailIndex.start()].strip()
                    coordinatorEmail = coordinatorInfo[emailIndex.start() + 7:].strip() 


                #Getting Program Location/Delivery Method
                deliveryMethod = program.find(string="Location/Delivery Method").findNext('ul').contents[0].nextSibling.get_text()

                gradProgram = GraduateProgram(programName, coordinatorName, coordinatorPhone, coordinatorEmail,deliveryMethod)
                

                if gradProgram not in graduateProgramList:
                        graduateProgramList.append(gradProgram)
        
        elif program.find(string="Coordinators") != None:

                coordinatorInfoList =between((program.find(string="Coordinators")),(program.find(string="Location/Delivery Method")))
                print(programName)
                #print(coordinatorInfoList[0])


                while(True):
                        if '-' in coordinatorInfoList[0]:
                                coordName = coordinatorInfoList[0].split('-')

                                programNameAndCon = programName
                                programNameAndCon += " ; "
                                programNameAndCon += coordinatorInfoList[1]

                        
                                  #Getting Program Location/Delivery Method
                                deliveryMethod = program.find(string="Location/Delivery Method").findNext('ul').contents[0].nextSibling.get_text()
                                del coordinatorInfoList[1]



                                gradProgram = GraduateProgram(programNameAndCon, coordinatorInfoList[0], coordinatorInfoList[1], coordinatorInfoList[2],deliveryMethod)

                        else:
                                gradProgram = GraduateProgram(programNameAndCon, coordinatorInfoList[0], coordinatorInfoList[1], coordinatorInfoList[2],deliveryMethod)


                        if gradProgram not in graduateProgramList:
                                graduateProgramList.append(gradProgram)

                        del coordinatorInfoList[0]
                        del coordinatorInfoList[0]
                        del coordinatorInfoList[0]

                        if len(coordinatorInfoList) == 0:
                                break

      


              


#for study in graduateProgramList:
        #print(study.programName, study.coordinatorName, study.coordinatorPhone, study.coordinatorEmail, study.deliveryMethod)