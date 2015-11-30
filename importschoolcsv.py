import csv
import mysql.connector


cnx = mysql.connector.connect(user='pisa', password='pisa2012',
                              host='127.0.0.1',
                              database='pisa')



headertypes = {}

def getsqltype(key,head):
    return htype

def getHeadInfo(head):
    headdict = {}
    headchoices = {}
    is_choices = False
    for line in open("INT_SCQ12_SPSS.sps"):
        if head in line:
            # If line says data type
            if "(F," in line or "(A)" in line:
                if "(F," in line:
                    headdict ["type"] ="float"
                else:
                    headdict ["type"] = "VARCHAR(12)"
            # Indicates start of options for this heading
            elif "/" in line and "Missing" not in line and is_choices == False:
                is_choices = True
            elif "Missing values" in line:
                missingvals = line.split()
                missingvals = missingvals[3][1:-2]
                missingvals = missingvals.split(",")
                headdict["missingvalues"] = missingvals
            else:
                headdict["Question Title"] = line
               # Indicates end of options for this heading    
        elif "/" in line and "Missing" not in line and is_choices == True:
            is_choices = False
            # Add the choices to a dictionary
        elif is_choices == True and not line == ".":
            choice = line.split()
            if len(choice) > 1:
                headchoices[choice[0]] = choice[1]
            else:
                is_choices = False
        if "99999" in line:
            is_choices = False
        if line == ".":
            is_choices = False
    headdict['choices'] = headchoices
    return headdict


started = False
finished = False
header = []
for line in open("INT_SCQ12_SPSS.sps"):
    if "CNT" in line and finished == False:
        started = True
    if "VER_SCQ" in line and started == True:
        head = line.split()[0]
        header.append(head)
        started = False
        finished = True
    if started == True and finished == False:
        head = line.split()[0]
        header.append(head)




for i, head in enumerate(header):
    headertypes[head] = getHeadInfo(head)
    
        
print headertypes


table_string = "CREATE TABLE `schools` ("
table_string += "`id` int NOT NULL AUTO_INCREMENT, "
    
for key in header:
    sqltype = headertypes[key]["type"]
    table_string += '`' + key + '` ' + sqltype 
    table_string += ','
table_string += "PRIMARY KEY (`id`)) ENGINE=InnoDB"

print table_string

cnx.raise_on_warnings = True

cursor = cnx.cursor()
cursor.execute(table_string)



add_school = "INSERT INTO schools ("
values = "VALUES ("
for key in header:
    add_school += '`' + key + '` ' 
    add_school += ','
    values += "%s, "
add_school = add_school[:-1]
values = values [:-2]
add_school += ")"
values += ")"
add_school += values

with open('school.csv', 'rb') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar = '"')
    for row in myreader:
#        print add_school
#        print row
        add_school = "INSERT INTO schools ("
        values = "VALUES ("
     
        
        newrow = []
        for i, item in enumerate(row):
       
            if not item == ' ':
                add_school += '`' + header[i] + '` ' 
                add_school += ','
                #values += "%s, "
                values += "'"+item+"', "
                #newrow.append(item)
        add_school = add_school[:-1]
        values = values [:-2]
        add_school += ") "
        values += ");"
        add_school += values
   
#        print add_school
        cursor = cnx.cursor()
        cursor.execute(add_school)
cnx.commit()
cursor.close()

cnx.close()


#outfile = open('schooldict.txt','a')
#outfile.write(str(headertypes))

#outfile = open('schooldicttwo.txt','a')
#for key in headertypes:
#    outfile.write(headertypes[key]['Question Title'])
#    outfile.write("\n")
    
