from collections import defaultdict
CasesDict = defaultdict(list)
in1=open("covid19.csv",'r')
L=in1.readlines()
in1.close
L2=L[1:]
for i in range(1, len(L2)):
	L2 = L[i].split(",")
	CasesDict[L2[6]].append(int(L2[4]))
print (CasesDict)