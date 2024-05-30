
#initialize Countries list

in1=open("covid19.csv",'r')
L=in1.readlines()
in1.close

#Build Countries List
def Build_Countries(Cntrys):

	L2=L[1:]
	for i in range(1, len(L2)):
		L2 = L[i].split(",")
		if L2[6] not in Cntrys:
			Cntrys.append(L2[6])

if __name__ == "__main__":
	Cntrys =[]
	Build_Countries(Cntrys)
	print(Cntrys)