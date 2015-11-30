import csv
import mysql.connector


cnx = mysql.connector.connect(user='pisa', password='pisa2012',
                              host='127.0.0.1',
                              database='pisa')



headertypes = {}
def getType(t):
    if is_number(t):
        if is_float(t):
            return "float"
        else:
            return "int"
    elif is_string(t):
        return "str"
    else:
        print "error"
        return "error"

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(f):
    if "." in f:
        return True
    else:
        return False

    
def is_string(s):
    try:
        str(s)
        return True
    except ValueError:
        return False
def getsqltype(key,head):
    htype = ""
    sixtyfour  = ['OCOD1','OCOD2','ST13Q01','ST15Q01','ST17Q01','ST19Q01','ST48Q01','ST55Q01',
                  'ST55Q02','ST55Q03','ST55Q04','ST62Q01','ST62Q02','ST62Q03','PROGN',
                  'ST62Q04','ST62Q05','ST62Q06','ST62Q07','ST62Q08','ST62Q09','ST62Q10','ST62Q11','ST62Q12',
                  'ST62Q13','ST62Q14','ST62Q15','ST62Q16','ST62Q17','ST62Q18','ST62Q19','COBN_S','COBN_M','COBN_F',
                  'IC11Q01','IC11Q02','IC11Q03','IC11Q04','IC11Q05','IC11Q06','IC11Q07',
                  'EC05Q01','EC07Q01','EC07Q02','EC07Q02','EC07Q03','EC07Q04','EC07Q05',
                  'EC08Q01','EC08Q02','EC08Q03','EC08Q04','LANGN','OCOD1','OCOD2','NC','TESTLANG']
    notsmallint = ['id','SUBNATIO','ST26Q15','ST26Q16','ST26Q17','STIDSTD']
    if head['headtype'] == 'float':
        htype = "FLOAT"
    elif head['headtype'] == 'int':
        if key in notsmallint:
            htype = "INT"
        else:
            htype = "SMALLINT"
    elif key in sixtyfour:
        htype = "VARCHAR(60)"
    else:
        htype = "VARCHAR(30)"
    return htype

     
    
    
with open('pisa2012.csv', 'rb') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar = '"')
    header = myreader.next()
    have_headings = False
    headings = header
    while have_headings == False:
        have_headings = True
        line = myreader.next()
        for i, head in enumerate(header):
            #headings.append(head)
            if not headertypes.has_key(head) and line[i] != "\\N":
                headertypes[head] = {'headtype':getType(line[i]),
                                     'value':line[i]}
            elif not headertypes.has_key(head):
                have_headings = False
        
print headertypes


table_string = "CREATE TABLE `pisa` ("
for key in headings:
    head = headertypes[key]
    sqltype = getsqltype(key,head)
    table_string += '`' + key + '` ' + sqltype 
    if key == "id":
        table_string += " NOT NULL AUTO_INCREMENT"
    table_string += ','
table_string += "PRIMARY KEY (`id`)) ENGINE=InnoDB"

print table_string


cursor = cnx.cursor()
cursor.execute(table_string)

cnx.close()
