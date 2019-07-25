import csv
import os
import json

def camelCase(st):
        output = ''.join(x for x in st.title() if x.isalnum())
        return output[0].lower() + output[1:]


inputFileName = "Invoice.csv"
outputFileName = os.path.splitext(inputFileName)[0] + "_2toCamel.csv"

with open(inputFileName, 'rb') as inFile, open(outputFileName, 'wb') as outfile:
        r = csv.reader(inFile, delimiter="|")
        w = csv.writer(outfile, delimiter=",")
        header = next(r)
        new_header = [camelCase(x) for x in header]
        next(r, None)
        w.writerow(new_header)
        for row in r:
            w.writerow(row)


   # data={}
    #with open(outputFileName) as csvFile:
        #csvReader=csv.DictReader(csvFile,delimiter="|")
        #for rows in csvReader:
                #id=['id']
                #data['id']=rows

    #jsonFilePath=os.path.splitext(inputFileName)[0] + +"_toJson.json"
    #with open(jsonFilePath,'w') as jsonFile:
        #jsonFile.write(json.dumps([row for row in data]))
