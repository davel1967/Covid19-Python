from datetime import date
import datetime

#a_date = datetime.date(2015, 10, 10)
a_date = date.today()
days = datetime.timedelta(5)

new_date = a_date - days
#Subtract 5 days from today

dateback = 120
catchup_day = date.today() - datetime.timedelta(dateback)
catchup_day_s = catchup_day.strftime("%D")
print("Catch Upto date = " + catchup_day.strftime("%D") )

Query_String = "DATE(a.created_on) >= SUBDATE(CURDATE(),$catchup_day_s) GROUP BY 1, 2, 3 ORDER BY 1 ASC "
print (Query_String)