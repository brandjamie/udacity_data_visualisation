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
#SC25Q05			"Parent Participation - Assistance building and grounds"
#SC34Q15			"School Leadership - Goal-oriented curriculum"
#SC27Q02			"Teacher intentions - Stay with well-known methods"
#SC16Q05			"Activities - Mathematics club "
#SC39Q07			"Quality Assurance - Student feed-back"

sqlselection = ['SCHOOLID','SCHSIZE','RATCMP15','PROPQUAL','PROPCERT','SMRATIO','RESPCUR','SC25Q05','SC34Q15','SC27Q02','SC16Q05','SC39Q07']
sqltitles = list(sqlselection)

















attitudes = [["ST88Q01","Attitude towards School - Does Little to Prepare Me for Life"],
["ST88Q02","Attitude towards School - Waste of Time"],
["ST88Q03","Attitude towards School - Gave Me Confidence"],
["ST88Q04","Attitude towards School- Useful for Job"],
["ST89Q02","Attitude toward School - Helps to Get a Job"],
["ST89Q03","Attitude toward School - Prepare for College"],
["ST89Q04","Attitude toward School - Enjoy Good Grades"],
["ST89Q05","Attitude toward School - Trying Hard is Important"]]





def getWeightedAveString (questionString):
    string = "SUM("
    string += questionString
    string += "*W_FSTUWT)/SUM(W_FSTUWT)"
    return string


pv1mathave = getWeightedAveString("PV1MATH")
pv2mathave = getWeightedAveString("PV2MATH")
pv3mathave = getWeightedAveString("PV3MATH")
pv4mathave = getWeightedAveString("PV4MATH")
pv5mathave = getWeightedAveString("PV5MATH")
avemath = '(' + pv1mathave + " + " + pv2mathave + " + "  + pv3mathave + " + " + pv4mathave + " + " + pv5mathave + ") / (5.0)"

pv1readave = getWeightedAveString("PV1READ")
pv2readave = getWeightedAveString("PV2READ")
pv3readave = getWeightedAveString("PV3READ")
pv4readave = getWeightedAveString("PV4READ")
pv5readave = getWeightedAveString("PV5READ")
averead = '(' + pv1readave + " + " + pv2readave + " + "  + pv3readave + " + " + pv4readave + " + " + pv5readave + ") / (5.0)"

pv1scieave = getWeightedAveString("PV1SCIE")
pv2scieave = getWeightedAveString("PV2SCIE")
pv3scieave = getWeightedAveString("PV3SCIE")
pv4scieave = getWeightedAveString("PV4SCIE")
pv5scieave = getWeightedAveString("PV5SCIE")
avescie = '(' + pv1scieave + " + " + pv2scieave + " + "  + pv3scieave + " + " + pv4scieave + " + " + pv5scieave + ") / (5.0)"







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
    
def getave(where = ""):
    selection = ["SCHOOLID",avemath,averead,avescie]
    groupby = "SCHOOLID"
    if not where == "":
        where += " AND "
    where += 'CNT = "United Kingdom"'
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



  


questionopts = ["Strongly Agree","Agree","Disagree","Strongly Disagree"]

pvs = getave()
questionaves = {}
for question in attitudes:
    thisq = question[0]
    questionaves[thisq] = {}
    for option in questionopts:
        string = thisq + ' = "' + option + '"'
        questionaves[thisq][option] = getave(string)

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











with open('ukschoolstwo.csv', 'wt') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        sqlselection.append('maths')
        sqlselection.append('read')
        sqlselection.append('scie')
        for question in attitudes:
            sqlselection.append(question[0]+"math")
            sqlselection.append(question[0]+"read")
            sqlselection.append(question[0]+"scie")
        sqlselection.append("option")
        csvwriter.writerow(sqlselection)
        for line in result:
            schoolid = int(line[0])
            #print type(line)
            newline = list(line)
            #print newline
            newline.append(pvs[schoolid]["math"])
            newline.append(pvs[schoolid]["read"])
            newline.append(pvs[schoolid]["scie"])
#            agree = list(newline)
#            sagree = list(newline)
#            disagree = list(newline)
#            sdisagree = list(newline)
#            newlines = {}
            for option in questionopts:
                #newlines[option] = list(newline)
                #thisline = newlines[option]
                thisline = list(newline)
                for question in attitudes:
                    #for option in questionopts:
                    if int(schoolid) in questionaves[question[0]][option]:
                        thisline.append(questionaves[question[0]][option][int(schoolid)]["math"])
                        thisline.append(questionaves[question[0]][option][int(schoolid)]["read"])
                        thisline.append(questionaves[question[0]][option][int(schoolid)]["scie"])
                    else:
                        thisline.append("0")
                        thisline.append("0")
                        thisline.append("0")
                thisline.append(option)
                csvwriter.writerow(thisline)

cnx.close()




#SELECT AVG(PV1MATH), AVG(PV2MATH), AVG(PV3MATH), AVG(PV4MATH), AVG(PV5MATH) FROM pisa WHERE CNT = "Korea";
