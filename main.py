import json
import urllib.request
import csv

url = "http://nflarrest.com/api/v1/team"

f = urllib.request.urlopen(url)
data = f.read().decode("utf-8")
readFile = json.loads(data)

with open("arrest.csv", "w") as arrestdata:
    csvwriter = csv.writer(arrestdata)
    count = 0
    for result in readFile:
        if count == 0:
            print(result)
            header = result.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(result.values())
