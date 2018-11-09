from genderize import getGenders
import csv

csvFile = open("myCsv.csv", "r", encoding = 'utf8')
csvReader = csv.reader(csvFile)
csvOut = open("outCsv.csv", "a", encoding = 'utf8')
csvWriter = csv.writer(csvOut)

for idx, row in enumerate(csvReader):
    if(idx < 1):
        continue

    names = row[2].split(",")
    print(idx)
    probList = []
    for name in names:
        singles = name.split(" ")
        total = 0
        prob = 0
        isFemale = False
        for i in singles:
            if(len(i) <= 2):
                continue
            print("Getting genderized")
            genderize = getGenders(i)[0]
            if(genderize[0] == "female"):
                sign = -1
                prob = -abs(prob)
                isFemale = True
            elif(genderize[0] == "male"):
                sign = 1
            else:
                sign = 0
            prob += float(genderize[1])*float(genderize[2])*sign
            total += int(genderize[2])
        if(isFemale):
            prob = -abs(prob)
        if(total == 0):
            prob = 696969
        elif prob is None:
            prob = 696969
        else:
            prob = prob/total
        if(prob is None):
            prob = 696969
        print(prob)
        probList.append(prob)
    row.append(probList)
    csvWriter.writerow(row)
    csvOut.flush()
