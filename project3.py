# Python libraries 
# from datetime import date
# from datetime import time
# from datetime import datetime
import urllib.request

def main():

    # File request from the internet
    # f = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")

    # Open file for reading
    f = open("http_access_log.txt","r")

    # inialize log request count 
    count = 0
    word = "GET"

    # Read lines in file
    searchlines = f.readlines()
    for x in searchlines:
        if word in x.split():
            count = count+1
    print("Total requests made in the time period of this log: " + str(count))

    # Close file
    f.close()
