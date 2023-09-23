#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import config
import os
import socket
import datetime
import time

from config import *				
from soa2filfuncs import soa2fil		# import the configuration generated by genconfig.py script
pgmver='2.0'
###################################################################
day 	= sys.argv[1:]                      	# see if index day is requestedd
execreq = sys.argv[2:]                      	# -e request
FlarmIDr = sys.argv[3:]                     	# -e request the FlarmID
if day and day[0].isdigit():                	# if provided and numeric
    idx = int(day[0])                       	# index day
else:
    idx = 0
                                            	# the FlarmID of the files to be reconstructed
FlarmID = ""
execopt = False
                                            	# if we ask to exec the buildIGC
if execreq and execreq[0] == "-e":
    if FlarmIDr:
        FlarmID = FlarmIDr[0].upper()       	# get the FlarmID
        if len(FlarmID) == 9:
           FlarmID = FalrmID[3:9]		# in case of form ICAxxxxxx
        execopt = True

# ---------------------------------------------------------------- #
print("\nUtility to get the api.soaringspot.com data and extract all the IGC files from the SoaringSpot server", pgmver)
print("==========================================================================================================\n\n")
print("Usage:   python soa2fil.py indexday  [-e FlarmID ]")
print("==================================================\n\n")
print("Index day: ", idx, "extract:", execopt,  "Flarm req: ",  FlarmID )
print("Reading data from clientid/secretkey files")
print("==========================================\n\n")
# ---------------------------------------------------------------- #
# ===== SETUP parameters =======================#
# where to get/store the IGC files
SARpath = config.SARpath
cwd = os.getcwd()			    	# get the current working directory
                                            	# where to find the clientid and secretkey files
secpath = cwd+"/SoaringSpot/"
                                            	# the subdirectory where to store the extracted files
# ==============================================#
hostname = socket.gethostname()		    	# hostname as control
print("Hostname:", hostname)
start_time = time.time()                    	# get the time now
utc = datetime.datetime.utcnow()            	# the UTC time
                                            	# print the time for information only
print("UTC Time is now:", utc)
date = utc.strftime("%Y-%m-%dT%H:%M:%SZ")   	# get the local time
print(date)                                 	#

local_time = datetime.datetime.now()        	# the local time
print("Local Time is now:", local_time)	    	# print the time for information only
fl_date_time = local_time.strftime("%Y%m%d")  	# get the local time
print("Config params.  SECpath:", secpath)

                                            	# open the file with the client id
f = open(secpath+"clientid")
client = f.read()                           	# read it
                                            	# clear the whitespace at the end
client = client.rstrip()
                                            	# open the file with the secret key
f = open(secpath+"secretkey")
secretkey = f.read()                        	# read it
                                            	# clear the whitespace at the end
secretkey = secretkey.rstrip().encode(encoding='utf-8')
soa2fil(client, secretkey, idx, FlarmID,execopt, prt=config.prt) # invoke the extractor
