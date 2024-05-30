import random
Alpha = 0.5
Patients = 30
NumDays = 19

PatientInfected = [[0 for x in range(NumDays)] for y in range(Patients)]
#print (len(PatientInfected), len(PatientInfected[0]))

Exposed = [0 for x in range(NumDays)]
Infected = [0 for x in range(NumDays)]
Recovered = [0 for x in range(NumDays)]
Suseptible = [0 for x in range(NumDays)]


#Initialize first 10 patients 
for i in range (0, 10):
	PatientInfected[i][0] = 1

#do something

for patient in range (0, Patients):
	for days in range (0, NumDays):	
		if (PatientInfected[patient][days-1] == 0):
			if ( (PatientInfected[patient-1][days-1] == 1 ) or (patient < 19 and (PatientInfected[patient+1][days-1] == 1)) ):
				probablity = random.random()
				if (probablity >= Alpha):
					Infected[days-1] += 1
				else:
					Exposed[days-1] += 1
			else:
#				print ("Patient: Prv, Nex, Susp", PatientInfected[patient][days-1], PatientInfected[patient-1][days-1], PatientInfected[patient+1][days-1], Suseptible[days])
				Suseptible[days-1] += 1
		else:
			if (days > 6):
				for loi in range (days-2 , days-6):
					print ("Len of Infection", loi)
					if (PatientInfected[patient][loi] == 0):
						Infected[days] += 1
					else:
						Recovered[days] += 1
			else:
				if (PatientInfected[patient][days-1] == 0):
						Infected[days-1] += 1
				else:
						Recovered[days-1] += 1		
#print (PatientInfected)
print ("Exposed", Exposed)
print ("Infected", Infected)
print ("Recovered", Recovered)
print ("Suseptible", Suseptible)