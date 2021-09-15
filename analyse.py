
import json
IPs = {}

f = open("../../DoWSimData/30day_1000user_10bot_2000rph.csv")

for line in f:
    if line.split(",")[0] in IPs:
        IPs[line.split(",")[0]] += 1
    else:
        IPs[line.split(",")[0]] = 1

f.close()

with open('out.txt', 'w') as file:
     file.write(json.dumps(IPs))

