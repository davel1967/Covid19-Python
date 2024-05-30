d = {}
in1=open("covid19.csv",'r')
L=in1.readlines()
in1.close
L2=L[1:]
for i in range(1, len(L2)):
	L2 = L[i].split(",")
	if L2[6] in d:
		d[L2[6]].append(L2[4])
	else:
		d[L2[6]] = []
		d[L2[6]].append(L2[4])
print(d)