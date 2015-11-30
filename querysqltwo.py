import csv
import mysql.connector

cnx = mysql.connector.connect(user='pisa', password='pisa2012',
                              host='127.0.0.1',
                              database='pisa')

table = "pisa"


questioncodes = {"ST81Q01":"Disciplinary Climate - Students Don't Listen","ST81Q02":"Disciplinary Climate - Noise and Disorder"}
adsfad = {"ST81Q03":"Disciplinary Climate - Teacher Has to Wait Until its Quiet",
          "ST81Q04":"Disciplinary Climate - Students Don't Work Well",
          "ST81Q05":"Disciplinary Climate - Students Start Working Late",
          "ST82Q01":"Vignette Teacher Support -Homework Every Other Day/Back in Time",
          "ST82Q02":"Vignette Teacher Support - Homework Once a Week/Back in Time",
          "ST82Q03":"Vignette Teacher Support - Homework Once a Week/Not Back in Time",
          "ST83Q01":"Teacher Support - Lets Us Know We Have to Work Hard",
          "ST83Q02":"Teacher Support - Provides Extra Help When Needed",
          "ST83Q03":"Teacher Support - Helps Students with Learning",
          "ST83Q04":"Teacher Support - Gives Opportunity to Express Opinions"}

qcodesb = {"ST84Q01":"Vignette Classroom Management - Students Frequently Interrupt/Teacher Arrives Early",
           "ST84Q02":"Vignette Classroom Management - Students Are Calm/Teacher Arrives on Time",
           "ST84Q03":"Vignette Classroom Management - Students Frequently Interrupt/Teacher Arrives Late",
           "ST85Q01":"Classroom Management - Students Listen",
           "ST85Q02":"Classroom Management - Teacher Keeps Class Orderly",
           "ST85Q03":"Classroom Management - Teacher Starts On Time",
           "ST85Q04":"Classroom Management - Wait Long to <Quiet Down>",
           "ST86Q01":"Student-Teacher Relation - Get Along with Teachers",
           "ST86Q02":"Student-Teacher Relation - Teachers Are Interested",
           "ST86Q03":"Student-Teacher Relation - Teachers Listen to Students",
           "ST86Q04":"Student-Teacher Relation - Teachers Help Students",
           "ST86Q05":"Student-Teacher Relation - Teachers Treat Students Fair",
           "ST87Q01":"Sense of Belonging - Feel Like Outsider",
           "ST87Q02":"Sense of Belonging - Make Friends Easily",
           "ST87Q03":"Sense of Belonging - Belong at School",
           "ST87Q04":"Sense of Belonging - Feel Awkward at School",
           "ST87Q05":"Sense of Belonging - Liked by Other Students",
           "ST87Q06":"Sense of Belonging - Feel Lonely at School",
           "ST87Q07":"Sense of Belonging - Feel Happy at School",
           "ST87Q08":"Sense of Belonging - Things Are Ideal at School",
           "ST87Q09":"Sense of Belonging - Satisfied at School",
           "ST88Q01":"Attitude towards School - Does Little to Prepare Me for Life",
           "ST88Q02":"Attitude towards School - Waste of Time",
           "ST88Q03":"Attitude towards School - Gave Me Confidence",
           "ST88Q04":"Attitude towards School- Useful for Job",
           "ST89Q02":"Attitude toward School - Helps to Get a Job",
           "ST89Q03":"Attitude toward School - Prepare for College",
           "ST89Q04":"Attitude toward School - Enjoy Good Grades",
           "ST89Q05":"Attitude toward School - Trying Hard is Important",
           "ST91Q01":"Perceived Control - Can Succeed with Enough Effort",
           "ST91Q02":"Perceived Control - My Choice Whether I Will Be Good",
           "ST91Q03":"Perceived Control - Problems Prevent from Putting Effort into School",
           "ST91Q04":"Perceived Control - Different Teachers Would Make Me Try Harder",
           "ST91Q05":"Perceived Control - Could Perform Well if I Wanted",
           "ST91Q06":"Perceived Control - Perform Poor Regardless",
           "ST93Q01":"Perseverance - Give up easily",
           "ST93Q03":"Perseverance - Put off difficult problems",
           "ST93Q04":"Perseverance - Remain interested",
           "ST93Q06":"Perseverance - Continue to perfection",
           "ST93Q07":"Perseverance - Exceed expectations"}



















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
    

#sqlselection = ['ST88Q03']
avemath = '(AVG(PV1MATH) + AVG(PV2MATH) + AVG(PV3MATH) + AVG(PV4MATH) + AVG(PV5MATH))/(5.0)'

averead = '(AVG(PV1READ) + AVG(PV2READ) + AVG(PV3READ) + AVG(PV4READ) + AVG(PV5READ))/(5.0)'

avescie = '(AVG(PV1SCIE) + AVG(PV2SCIE) + AVG(PV3SCIE) + AVG(PV4SCIE) + AVG(PV5SCIE))/(5.0)'




sqlnames = ['Answer','Ave Math Score','Ave Rdg Score','Ave Sci Score']
#sqlselection = ['PV1MATH', 'PV2MATH', 'PV3MATH', 'PV4MATH', 'PV5MATH']


            
where = 'CNT = "United Kingdom"'

results = {}


for key in questioncodes:
    sqlselection = [key,avemath,averead,avescie]
    groupby = key
    sqlstring = makestring(sqlselection,where,groupby)
    #print sqlstring
    cursor = cnx.cursor()
    cursor.execute(sqlstring)
    result = cursor.fetchall()
    results[key]=result

            

with open('tmp.csv', 'wt') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #csvwriter.writerow(sqlselection)
        for key in questioncodes:
            result = results[key]
            csvwriter.writerow(["",])
            csvwriter.writerow([key,])
            csvwriter.writerow([questioncodes[key],])
            csvwriter.writerow(sqlnames)
            for line in result:
                csvwriter.writerow(line)

cnx.close()




#SELECT AVG(PV1MATH), AVG(PV2MATH), AVG(PV3MATH), AVG(PV4MATH), AVG(PV5MATH) FROM pisa WHERE CNT = "Korea";
