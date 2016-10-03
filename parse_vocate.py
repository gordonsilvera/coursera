import re
import csv

filename = "C:/Users/gordon-local/Downloads/vocate (update).sql"
text_file = open(filename, "r")
lines = text_file.readlines()

csvOutFile = 'C:/Users/gordon-local/Desktop/Vocate_DataList.csv'
csvOutTest = open(csvOutFile, 'wb')
csvWrite = csv.writer(csvOutTest, delimiter=',',quoting=csv.QUOTE_MINIMAL)
csvWrite.writerow(['dataset', 'variable', 'variable_type','variable_type2']) #column names

i= 0
for i in range(0,len(lines)):

    match1 = re.match(r'CREATE TABLE.*\(', lines[i])
    if match1 is not None:
        matchSplit1 = match1.group(0).split()
        #print matchSplit1[2]

        x = 0
        e = 0
        while e < 1:

            match2 = re.match(r".*,", lines[i + x])
            matchEnd = re.match(r".*\);", lines[i + x])

            if match2 is not None:
                matchSplit2 = match2.group(0).split()

                if 'CONSTRAINT' in matchSplit2:
                    matchSplit2.remove('CONSTRAINT')
                if 'NOT' in matchSplit2:
                    matchSplit2.remove('NOT')
                if 'NULL' in matchSplit2:
                    matchSplit2.remove('NULL')
                if 'NULL,' in matchSplit2:
                    matchSplit2.remove('NULL,')
                if 'CHECK' in matchSplit2:
                    matchSplit2.remove('CHECK')
                if 'time' in matchSplit2:
                    matchSplit2.remove('time')
                if 'with' in matchSplit2:
                    matchSplit2.remove('with')
                if 'zone,' in matchSplit2:
                    matchSplit2.remove('zone,')
                if 'zone' in matchSplit2:
                    matchSplit2.remove('zone')
                if '0)),' in matchSplit2:
                    matchSplit2.remove('0)),')
                if '>=' in matchSplit2:
                    matchSplit2.remove('>=')

                matchSplit2.insert(0, matchSplit1[2])
                print matchSplit2
                csvWrite.writerow(matchSplit2)

            if matchEnd is not None:
                e = 1

            x=x+1
        

csvOutTest.close()
