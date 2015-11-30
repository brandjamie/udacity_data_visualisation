import csv
import mysql.connector
import math
cnx = mysql.connector.connect(user='pisa', password='pisa2012',
                              host='127.0.0.1',
                              database='pisa')









table = "schools"
sqlselection = ['SCHOOLID','SC14Q01','SC14Q02','SC14Q03','SC14Q04','SC14Q05','SC14Q06','SC14Q07','SC14Q08','SC14Q09','SC14Q10']



avemath = '(AVG(PV1MATH) + AVG(PV2MATH) + AVG(PV3MATH) + AVG(PV4MATH) + AVG(PV5MATH))/(5.0)'

averead = '(AVG(PV1READ) + AVG(PV2READ) + AVG(PV3READ) + AVG(PV4READ) + AVG(PV5READ))/(5.0)'

avescie = '(AVG(PV1SCIE) + AVG(PV2SCIE) + AVG(PV3SCIE) + AVG(PV4SCIE) + AVG(PV5SCIE))/(5.0)'








#Create string for sql query
def makestring(sqlselection,where = False,groupby = False,table = "pisa"):
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
    resultdict = {}
    for line in result:
        thisdict = {"math":line[1],"read":line[2],"scie":line[3]}
        resultdict[line[0]]=thisdict

    return resultdict


        


def getPercentiles():
    mathscores = []
    readscores = []
    sciescores = []
    for schoolid in pvs:
        item = pvs[schoolid]
        mathscores.append(item["math"])
        readscores.append(item["read"])
        sciescores.append(item["scie"])
    mathscores.sort()
    readscores.sort()
    sciescores.sort()
    numofschools = len(mathscores)
    pmath = {25:mathscores[int(math.ceil(numofschools*.25))],
             50:mathscores[int(math.ceil(numofschools*.50))],
             75:mathscores[int(math.ceil(numofschools*.75))]}
    pread = {25:readscores[int(math.ceil(numofschools*.25))],
             50:readscores[int(math.ceil(numofschools*.50))],
             75:readscores[int(math.ceil(numofschools*.75))]}
    pscie = {25:sciescores[int(math.ceil(numofschools*.25))],
             50:sciescores[int(math.ceil(numofschools*.50))],
             75:sciescores[int(math.ceil(numofschools*.75))]}
    percentiles = {"math":pmath,"read":pread,"scie":pscie}
    return percentiles



pvs = getpvs()

percentiles = getPercentiles()


print "*************************"
print percentiles
print "*************************"

where = 'CNT = "GBR"'
    
groupby = False
sqlstring = makestring(sqlselection,where,groupby,table)
#print sqlstring
cursor = cnx.cursor()
cursor.execute(sqlstring)
schoolresult = cursor.fetchall()



def getSchool(schoolid):
    thisSchool = ()
    for line in schoolresult:
        if schoolid == int(line[0]):
            thisSchool = list(line)
            thisSchool.append(getSchoolPercentile(schoolid,"math"))
            thisSchool.append(getSchoolPercentile(schoolid,"read"))
            thisSchool.append(getSchoolPercentile(schoolid,"scie"))
            
     #       thisSchool.append(pvs[schoolid]["math"])
     #       thisSchool.append(pvs[schoolid]["read"])
     #       thisSchool.append(pvs[schoolid]["scie"])
     
    return tuple(thisSchool)

def getSchoolPercentile(schoolid,subject):
    thisscore = pvs[schoolid][subject]
    thisP = percentiles[subject]
    thisPercentile = 0
    if thisscore <= thisP[25]:
        thisPercentile = 0
    elif thisscore <= thisP[50]:
        thisPercentile = 1
    elif thisscore <= thisP[75]:
        thisPercentile = 2
    else:
        thisPercentile = 3
    return thisPercentile


# with open('ukschoolsthree.csv', 'wt') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=',',
#                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
sqlselection.append('schoolmath')
sqlselection.append('schoolread')
sqlselection.append('schoolscie')
#         print type(result)
#         csvwriter.writerow(sqlselection)
#         for line in result:
#             schoolid = int(line[0])
#             #print type(line)
#             newline = list(line)
#             #print newline
#             newline.append(pvs[schoolid]["math"])
#             newline.append(pvs[schoolid]["read"])
#             newline.append(pvs[schoolid]["scie"])
            
#             csvwriter.writerow(newline)

# cnx.close()













table = "pisa"


questioncodes = ["SCHOOLID",
                 "W_FSTUWT",
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
                 "ST91Q06"]
                



mathpv = '(PV1MATH + PV2MATH + PV3MATH + PV4MATH + PV5MATH)/(5.0)'

readpv = '(PV1READ + PV2READ + PV3READ + PV4READ + PV5READ)/(5.0)'

sciepv = '(PV1SCIE + PV2SCIE + PV3SCIE + PV4SCIE + PV5SCIE)/(5.0)'

sqlselectiontwo = list(questioncodes)



    



where = 'CNT = "United Kingdom"'

sqlselectiontwo.append(mathpv)    
sqlselectiontwo.append(readpv)    
sqlselectiontwo.append(sciepv)    
    
groupby = False
sqlstring = makestring(sqlselectiontwo,where,groupby,table)
#print sqlstring
cursor = cnx.cursor()
cursor.execute(sqlstring)
result = cursor.fetchall()

sqlselection 
print sqlselection


with open('uk_studentsThree.csv', 'wt') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        questioncodes.append('maths')
        questioncodes.append('read')
        questioncodes.append('scie')
        questioncodes = questioncodes + sqlselection
        csvwriter.writerow(questioncodes)
        lineno = 0
        for line in result:
            if lineno < 20:
                print line[3]
                lineno = lineno + 1
            if not line[3] == None:
         
                thisschoolid = int(line[0])
                thisschooldata = getSchool(thisschoolid)
                csvwriter.writerow(line + thisschooldata)

cnx.close()

