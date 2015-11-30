import csv
import mysql.connector
cnx = mysql.connector.connect(user='pisa', password='pisa2012',
                              host='127.0.0.1',
                              database='pisa')

table = "schools"
## Query for getting school data:
#SCHOOLID    "School ID 7-digit (region ID + stratum ID + 3-digit school ID)"

# SC14Q10			"Shortage - Library materials"

# SC14Q09			"Shortage - Computer software"

# SC14Q08			"Shortage - Internet connectivity"

# SC14Q05			"Shortage - Science lab equipment"

# SC14Q04			"Shortage - Other teachers"

# SC14Q07			"Shortage - Computers for instruction"

# SC14Q06			"Shortage - Instructional materials"

# SC14Q01			"Shortage - Science teachers"

# SC14Q03			"Shortage - <Test language> teachers"

# SC14Q02			"Shortage - Maths teachers"

sqlselection = ['SCHOOLID','SC14Q01','SC14Q02','SC14Q03','SC14Q04','SC14Q05','SC14Q06','SC14Q07','SC14Q08','SC14Q09','SC14Q10']



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











with open('ukschoolsthree.csv', 'wt') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        sqlselection.append('schoolmath')
        sqlselection.append('schoolread')
        sqlselection.append('schoolscie')
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
