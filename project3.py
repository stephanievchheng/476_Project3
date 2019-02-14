# Python libraries 
import urllib.request
import re
from datetime import date
from datetime import time
from datetime import datetime

# regex format array  
regex = r'(.*?) - - \[(.*)\] \"(.*?) (.*?\..*?) (HTTP\/\d\.\d)\" (\d*) (\d*)'

# File request from the internet
f = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")

# Decode binary into text 
log = f.read()
log = log.decode()

# Inialize log request counts 
logcount = 0
jancount = 0
febcount = 0
marcount = 0
aprcount = 0
maycount = 0
juncount = 0
julcount = 0
augcount = 0
sepcount = 0
octcount = 0
novcount = 0
deccount = 0

# Define variables to use to search later
word = "GET"
month1 = "Jan"
month2 = "Feb"
month3 = "Mar"
month4 = "Apr"
month5 = "May"
month6 = "Jun"
month7 = "Jul"
month8 = "Aug"
month9 = "Sep"
month10 = "Oct"
month11 = "Nov"
month12 = "Dec"

# Read lines in file
lines = log.splitlines()
for line in lines:
        match = re.match(regex, line)
        if match:
                #print(match.group(3))
                # Start counting requests 
                if word in match.group(3):
                        logcount = logcount+1

                if month1 in match.group(2):
                        jancount = jancount+1
                if month2 in match.group(2):
                        febcount = febcount+1
                if month3 in match.group(2):
                        marcount = marcount+1
                if month4 in match.group(2):
                        aprcount = aprcount+1
                if month5 in match.group(2):
                        maycount = maycount+1
                if month6 in match.group(2):
                        juncount = juncount+1
                if month7 in match.group(2):
                        julcount = julcount+1
                if month8 in match.group(2):
                        augcount = augcount+1
                if month9 in match.group(2):
                        sepcount = sepcount+1
                if month10 in match.group(2):
                        octcount = octcount+1
                if month11 in match.group(2):
                        novcount = novcount+1
                if month12 in match.group(2):
                        deccount = deccount+1
                      

print("Total requests made during the time period of this log: " + str(logcount))

print("Number of requests made on each month:")
print("Jan: " + str(jancount))
print("Feb: " + str(febcount))
print("Mar: " + str(marcount))
print("Apr: " + str(aprcount))
print("May: " + str(maycount))
print("Jun: " + str(juncount))
print("Jul: " + str(julcount))
print("Aug: " + str(augcount))
print("Sep: " + str(sepcount))
print("Oct: " + str(octcount))
print("Nov: " + str(novcount))
print("Dec: " + str(deccount))


print("Percentage of requests not successful: ")


print("Percentage of requests redirected: ")


print("Most requested file: ")


print("Least requested file: ")


# Close file
f.close()
