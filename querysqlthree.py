import csv
import mysql.connector
cnx = mysql.connector.connect(user='pisa', password='pisa2012',
                              host='127.0.0.1',
                              database='pisa')

table = "schools"
## Query for getting school data:
#SCHOOLID    "School ID 7-digit (region ID + stratum ID + 3-digit school ID)"
#SCHSIZE   	"Total school enrolment"
#RATCMP15  	"Ratio of computers for education and number of students in the <national modal grade for 15-year-olds>"
#PROPQUAL  	"Proportion of teachers with ISCED 5A"
#PROPCERT  	"Proportion of certified teachers"
#SMRATIO   	"Maths Teacher-student ratio"
#RESPCUR			"Index of school responsibility for curriculum and assessment"


sqlselection = ['SCHOOLID','SCHSIZE','RATCMP15','PROPQUAL','PROPCERT','SMRATIO','RESPCUR']



avemath = '(AVG(PV1MATH) + AVG(PV2MATH) + AVG(PV3MATH) + AVG(PV4MATH) + AVG(PV5MATH))/(5.0)'

averead = '(AVG(PV1READ) + AVG(PV2READ) + AVG(PV3READ) + AVG(PV4READ) + AVG(PV5READ))/(5.0)'

avescie = '(AVG(PV1SCIE) + AVG(PV2SCIE) + AVG(PV3SCIE) + AVG(PV4SCIE) + AVG(PV5SCIE))/(5.0)'





#Create string for sql query
def makestring(sqlselection,where,groupby,table):
    qstring = ""
    qstring += "SELECT"
    for item in sqlselection:
        qstring += " " +item + ","
    # remove last comma
    qstring = qstring[:-1]
    qstring += " FROM " + table
    if not where == False:
        qstring += " WHERE " + where
    if not groupby == False:
        qstring += " GROUP BY " + groupby
    qstring += ";"
    return qstring
    
def getpvs():
    selection = ["SCHOOLID",avemath,averead,avescie]
    groupby = "SCHOOLID"
    where = 'CNT = "United Kingdom"'
    sqlstring = makestring(selection,where,groupby,"pisa")
    print sqlstring
    cursor = cnx.cursor()
    cursor.execute(sqlstring)
    result = cursor.fetchall()
    print result
    resultdict = {}
    for line in result:
        thisdict = {"math":line[1],"read":line[2],"scie":line[3]}
        resultdict[line[0]]=thisdict

    return resultdict


pvs = getpvs()
print pvs

where = 'CNT = "GBR"'

#sqlselection.append(mathpv)    
#sqlselection.append(readpv)    
#sqlselection.append(sciepv)    
    
groupby = False
sqlstring = makestring(sqlselection,where,groupby,table)
#print sqlstring
cursor = cnx.cursor()
cursor.execute(sqlstring)
result = cursor.fetchall()

print sqlselection











with open('ukschools.csv', 'wt') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        sqlselection.append('maths')
        sqlselection.append('read')
        sqlselection.append('scie')
        print type(result)
        csvwriter.writerow(sqlselection)
        for line in result:
            schoolid = int(line[0])
            #print type(line)
            newline = list(line)
            #print newline
            newline.append(pvs[schoolid]["math"])
            newline.append(pvs[schoolid]["read"])
            newline.append(pvs[schoolid]["scie"])
            
            csvwriter.writerow(newline)

cnx.close()




#SELECT AVG(PV1MATH), AVG(PV2MATH), AVG(PV3MATH), AVG(PV4MATH), AVG(PV5MATH) FROM pisa WHERE CNT = "Korea";
