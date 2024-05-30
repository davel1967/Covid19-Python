#smahade3:04092020:covid19.py

#a
"""read the data set, store specific fields in lists and dictionaries, calculate case fatality rate and crude mortality rate"""
#b
import sys
import countries

#Initialize cases and deaths dictionary


Dcases = {}
Ddeaths = {}
Dpop = {}

in1=open("covid19.csv",'r')
L=in1.readlines()
in1.close

#Initialize Countries List
Countries = []

#Call countries.py Module to build Countries List

countries.Build_Countries(Countries)

#
#Build Deaths Dictionary
#

L2=L[1:]
for i in range(1, len(L2)):
	L2 = L[i].split(",")
	if L2[6] in Ddeaths:
		Ddeaths[L2[6]].append(L2[5])
	else:
		Ddeaths[L2[6]] = []
		Ddeaths[L2[6]].append(L2[5])
#
#Build Cases Dictionary	
#
L2=L[1:]
for i in range(1, len(L2)):
	L2 = L[i].split(",")
	if L2[6] in Dcases:
		Dcases[L2[6]].append(L2[4])
	else:
		Dcases[L2[6]] = []
		Dcases[L2[6]].append(L2[4])
#
#Build Population Dictionary	
#
L2=L[1:]
for i in range(1, len(L2)):
	L2 = L[i].split(",")
	if L2[6] not in Dpop:
		Dpop[L2[6]]= []
		Dpop[L2[6]].append(int(L2[9]))

def total_cases(Country):
	CaseList = []
	CaseList = Dcases[Country]
	TotalCasesInACountry=0
	k=0
	while k < len(CaseList):
		TotalCasesInACountry += int(CaseList[k])
		k +=1
	return TotalCasesInACountry

#
#Total Deaths Function		
#
def total_deaths(Country):
	DeathsList = []
	DeathsList = Ddeaths[Country]
	TotalDeathsInACountry=0
	k=0
	while k < len(DeathsList):
		TotalDeathsInACountry += int(DeathsList[k])
		k +=1
	return TotalDeathsInACountry
#
#Defining CFR Function
#
def cfrfunc(Country):
	cfr=0
	cfr = (float(total_deaths(Country))/float(total_cases(Country)))*100
	if __name__ == "__main__":
		print("The CFR is: ",format(cfr, '.2f'))
	return cfr
#
#build daily cases
#
def daily_case_deaths(Country):
	CaseList = []
	CaseList = Dcases[Country]
	DeathsList = []
	DeathsList = Ddeaths[Country]
	k=0
	if __name__ == "__main__":	
		print("Cases and Deaths")
	while k < len(CaseList):
		if __name__ == "__main__":
			print(CaseList[k],DeathsList[k])	
		k +=1

#define CMR function
def cmrfunc(Country):
	cmr=0
	popu_list = Dpop[Country]
	popu = popu_list[0]
	cmr = (float(total_deaths(Country))/float(popu))*100000
	if __name__ == "__main__":
		print("The CMR is ", format(cmr, '1.2e'))
	return cmr	

if __name__ == "__main__":
	InputCountry = sys.argv[1]
	daily_case_deaths(InputCountry)
	print("Total Cases:", total_cases(InputCountry))
	print("Total Deaths:", total_deaths(InputCountry))
	cntrypopulist=Dpop[InputCountry]
	cntrypopu=cntrypopulist[0]
	print("Total Population:", cntrypopu)

	cfrfunc(InputCountry)
	cmrfunc(InputCountry)

#total_deaths(InputCountry)
#total_cases(InputCountry)


#CaseList = []
#for Country in dcases:
#	CaseList = dcases[Country]
#	TotalCasesInACountry=0
#	k=0
#	while k < len(CaseList):
#		TotalCasesInACountry += int(CaseList[k])
#		k +=1
#	print(Country, TotalCasesInACountry)

if __name__ == "__total_cases__":
	total_cases(InputCountry)

if __name__ == "__CFR__":
	cfrfunc(InputCountry)