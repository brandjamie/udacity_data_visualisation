import csv
import mysql.connector

cnx = mysql.connector.connect(user='pisa', password='pisa2012',
                              host='127.0.0.1',
                              database='pisa')

table = "pisa"


questioncodes = ["SCHOOLID",
                 "ST04Q01",
                 "ST86Q01",
                 "ST86Q02",
                 "ST86Q03",
                 "ST86Q04",
                 "ST86Q05",
                 "ST87Q01",
                 "ST87Q02",
                 "ST87Q03",
                 "ST87Q04",
                 "ST87Q05",
                 "ST87Q06",
                 "ST87Q07",
                 "ST87Q08",
                 "ST87Q09",
                 "ST88Q01",
                 "ST88Q02",
                 "ST88Q03",
                 "ST88Q04",
                 "ST89Q02",
                 "ST89Q03",
                 "ST89Q04",
                 "ST89Q05",
                 "ST91Q01",
                 "ST91Q02",
                 "ST91Q03",
                 "ST91Q04",
                 "ST91Q05",
                 "ST91Q06",
                 "ST93Q01",
                 "ST93Q03",
                 "ST93Q04",
                 "ST93Q06",
                 "ST93Q07"]




mathpv = '(PV1MATH + PV2MATH + PV3MATH + PV4MATH + PV5MATH)/(5.0)'

readpv = '(PV1READ + PV2READ + PV3READ + PV4READ + PV5READ)/(5.0)'

sciepv = '(PV1SCIE + PV2SCIE + PV3SCIE + PV4SCIE + PV5SCIE)/(5.0)'













#Create string for sql query
def makestring(sqlseletion,where = False,groupby = False):
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
    



where = 'CNT = "United Kingdom"'

sqlselection.append(mathpv)    
sqlselection.append(readpv)    
sqlselection.append(sciepv)    
    
groupby = False
sqlstring = makestring(sqlselection,where,groupby)
#print sqlstring
cursor = cnx.cursor()
cursor.execute(sqlstring)
result = cursor.fetchall()

print sqlselection

with open('uk_students.csv', 'wt') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        sqlselection += 'maths'
        sqlselection += 'read'
        sqlselection += 'scie'
        
        csvwriter.writerow(sqlselection)
        for line in result:
            print len(line)
            csvwriter.writerow(line)

cnx.close()




#SELECT AVG(PV1MATH), AVG(PV2MATH), AVG(PV3MATH), AVG(PV4MATH), AVG(PV5MATH) FROM pisa WHERE CNT = "Korea";
