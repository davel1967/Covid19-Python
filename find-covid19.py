import sys
import covid19

o_file= open("covid19-CFR-results.dat", "w+")
o_file2= open("covid19-CMR-results.dat", "w+")

L1=covid19.L
L3=L1[1:]

d_f1=""		#declare an empty list of countries

print("CFR for Counteries that fit the criteria")
for i in range(1, len(L3)):
	L3 = L1[i].split(",")
	casesInACntry=covid19.total_cases(L3[6])
	if ( (L3[6] != d_f1) and (casesInACntry  > 100 ) and (covid19.cfrfunc(L3[6]) > 8) ):
			print(L3[6],format(covid19.cfrfunc(L3[6]), '.2f') )
			o_file.write("{0:15}".format(L3[6]))
			o_file.write(format(covid19.cfrfunc(L3[6]), '.2f') )
			o_file.write("\n")
			d_f1=L3[6]
o_file.close()

print("CMR for Counteries that fit the criteria")
d_f1=""			#reset d_f1 list
L3=L1[1:] 		#reset L3
for i in range(1, len(L3)):
	L3 = L1[i].split(",")
	casesInACntry=covid19.total_cases(L3[6])
	if ( (L3[6] != d_f1) and (casesInACntry  > 100 ) and (covid19.cmrfunc(L3[6]) > 20) ):
			print(L3[6],format(covid19.cmrfunc(L3[6]), '1.2e') )
			o_file2.write("{0:15}".format(L3[6]))
			o_file2.write(format(covid19.cmrfunc(L3[6]), '1.2e') )
			o_file2.write("\n")
			d_f1=L3[6]
o_file2.close()