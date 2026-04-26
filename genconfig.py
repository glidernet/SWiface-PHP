#!/usr/bin/python3
#
# configuration for the Silent Wings OGN interface the online part
#

#-------------------------------------
# OGN-Silent Wings interface --- Settings
#-------------------------------------
#
#-------------------------------------
# Setting values from config.ini file
#-------------------------------------
#
import socket
import os
import datetime
from   gistfuncs  import obscure
from configparser import ConfigParser
configdir = os.getenv('CONFIGDIR')
if configdir == None:
    configdir = '/etc/local/'
configfile = configdir+'SWSconfig.ini'

datafile = open("config.py", "w")
tailfile = open("configtail.txt", "r")
datafile.write("# SWS configuration file \n")
SWSserver = 'http://localhost'
hostname = socket.gethostname()
datafile.write("# -*- coding: UTF-8 -*-")
datafile.write("# SWS hostname: "+hostname+"\n")
datafile.write("# SWS config file: "+configfile+"\n")
datafile.write("# Config generated: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" \n")
cfg = ConfigParser()
cfg.read(configfile)

try:
    cucFileLocation = cfg.get(
        'server', 'cucFileLocation').strip("'").strip('"')
except:
    cucFileLocation = "/var/www/html/cuc/"

DBpath = cfg.get('server', 'DBpath').strip("'").strip('"')
try:
    SARpath = cfg.get('server', 'SARpath').strip("'").strip('"')
except:
    SARpath = DBpath
MySQLtext = cfg.get('server', 'MySQL').strip("'").strip('"')
DBhost = cfg.get('server', 'DBhost').strip("'").strip('"')
DBuser = cfg.get('server', 'DBuser').strip("'").strip('"')
DBpasswd = cfg.get('server', 'DBpasswd').strip("'").strip('"')
origDBpasswd=DBpasswd
DBpasswd = obscure(DBpasswd.encode())
try:
    DBuserread = cfg.get('server', 'DBuserread').strip("'").strip('"')
except:
    DBuserread = DBuser
try:
    DBpasswdread = cfg.get('server', 'DBpasswdread').strip("'").strip('"')
    DBpasswdread = obscure(DBpasswdread.encode())
except:
    DBpasswdread = obscure(origDBpasswd.encode())
try:
    SWSserver = cfg.get('server', 'SWSserver').strip("'").strip('"')
except:
    SWSserver = 'http://localhost/'
try:
    TPTserver = cfg.get('server', 'TPTserver').strip("'").strip('"')
except:
    TPTserver = SWSserver
DBname = cfg.get('server', 'DBname').strip("'").strip('"')
try:
    DBtable = cfg.get('server', 'DBtable').strip("'").strip('"')
except:
    DBtable = "OGNDATA"

SQLite3 = cfg.get('server', 'SQLite3').strip("'").strip('"')
Initials = cfg.get('server', 'Initials').strip("'").strip('"')

locname = cfg.get('location', 'location_name').strip("'").strip('"')
eventname1 = cfg.get('location', 'eventname1').strip("'").strip('"')
eventname2 = cfg.get('location', 'eventname2').strip("'").strip('"')

eventdesc1 = cfg.get('location', 'eventdesc1').strip("'").strip('"')
eventdesc2 = cfg.get('location', 'eventdesc2').strip("'").strip('"')
#
try:
    loclatitude = cfg.get('location', 'location_latitude').strip("'").strip('"')
except:
    loclatitude = ''
try:
    loclongitud = cfg.get('location', 'location_longitud').strip("'").strip('"')
except:
    loclongitud = ''
#
try:
    PicPilots = cfg.get('location', 'PicPilots').strip("'").strip('"')
except:
    PicPilots = ' '
try:
    DDBhost = cfg.get('server', 'DDBhost').strip("'")
except:
    DDBhost = 'ddb.acasado.name'

try:
    DDBport = cfg.get('server', 'DDBport').strip("'")
except:
    DDBport = '60082'

try:
    DDBurl1 = cfg.get('server', 'DDBurl1').strip("'")
except:
    DDBurl1 = 'http://ddb.acasado.name:60082/download/?j=2'

try:
    DDBurl2 = cfg.get('server', 'DDBurl2').strip("'")
except:
    DDBurl2 = 'http://DDB.glidernet.org/download/?j=2'

try:
    GIST = cfg.get('server', 'GIST').strip("'")
except:
    GIST = 'False'

try:
    GIST_USER = cfg.get('server', 'GIST_USER').strip("'")
    GIST = 'True'
except:
    GIST_USER = ''

try:
    GIST_TOKEN = cfg.get('server', 'GIST_TOKEN').strip("'")
    GIST = 'True'
except:
    GIST_TOKEN = ''

origGIST_TOKEN=GIST_TOKEN
GIST_TOKEN = obscure(GIST_TOKEN.encode())

try:
    clientid = cfg.get('server', 'clientid').strip("'")
except:
    clientid = ''
try:
    secretkey = cfg.get('server', 'secretkey').strip("'")
except:
    secretkey = ''
try:
    OGNTRACKERS = cfg.get('server', 'OGNTRACKERS').strip("'")
except:
    OGNTRACKERS = 'False'
try:
    DISTHOME = cfg.get('server', 'DISTHOME').strip("'")
except:
    DISTHOME = ''
try:
    DIFFALT = cfg.get('server', 'DIFFALT').strip("'")
except:
    DIFFALT = ''
try:
    DIFFAVG = cfg.get('server', 'DIFFAVG').strip("'")
except:
    DIFFAVG = ''
try:
    FAIPWD = cfg.get('server', 'FAIPWD').strip("'")
except:
    FAIPWD = ''



datafile.write("cucFileLocation='"+cucFileLocation+"' \n")
datafile.write("DBpath='"+DBpath+"' \n")
datafile.write("SARpath='"+SARpath+"' \n")
datafile.write("DBhost='"+DBhost+"' \n")
datafile.write("DBname='"+DBname+"' \n")
datafile.write("DBtable='"+DBtable+"' \n")
datafile.write("SQLite3='"+SQLite3+"' \n")
datafile.write("DBuser='"+DBuser+"' \n")
datafile.write("DBpasswd='"+DBpasswd.decode()+"' \n")
datafile.write("DBuserread='"+DBuserread+"' \n")
datafile.write("DBpasswdread='"+DBpasswdread.decode()+"' \n")
datafile.write("MySQL="+MySQLtext+" \n")
datafile.write("Initials='"+Initials+"' \n")
datafile.write("SWSserver='"+SWSserver+"' \n")
datafile.write("TPTserver='"+TPTserver+"' \n")
datafile.write("eventname1='"+eventname1+"' \n")
datafile.write("eventname2='"+eventname2+"' \n")
datafile.write("eventdesc1='"+eventdesc1+"' \n")
datafile.write("eventdesc2='"+eventdesc2+"' \n")
datafile.write("loclatitude='"+loclatitude+"' \n")
datafile.write("loclongitud='"+loclongitud+"' \n")
datafile.write("locname='"+locname+"' \n")
datafile.write("PicPilots='"+PicPilots+"' \n")
datafile.write("DDBhost='"+DDBhost+"' \n")
datafile.write("DDBport='"+DDBport+"' \n")
datafile.write("DDBurl1='"+DDBurl1+"' \n")
datafile.write("DDBurl2='"+DDBurl2+"' \n")
datafile.write("GIST="+GIST+" \n")
datafile.write("GIST_USER='"+GIST_USER+"' \n")
datafile.write("GIST_TOKEN='"+GIST_TOKEN.decode()+"' \n")
datafile.write("clientid='"+clientid+"' \n")
datafile.write("secretkey='"+secretkey+"' \n")
datafile.write("OGNTRACKERS="+OGNTRACKERS+" \n")
datafile.write("DISTHOME='"+DISTHOME+"' \n")
datafile.write("DIFFALT='"+DIFFALT+"' \n")
datafile.write("DIFFAVG='"+DIFFAVG+"' \n")
datafile.write("FAIPWD='"+FAIPWD+"' \n")
datafile.write("prt=False \n")

# --------------------------------------#
datafile.write(tailfile.read())
datafile.close()
tailfile.close()
datafile = open("config.php", "w")
datafile.write("<?php \n")
datafile.write("# SWS configuration file \n")
datafile.write("# -*- coding: UTF-8 -*-")
datafile.write("# SWS hostname: "+hostname+"\n")
datafile.write("# SWS config file: "+configfile+"\n")
datafile.write("# Config generated: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" \n")
datafile.write("$DBpath='"+DBpath+"';\n")
datafile.write("$SARpath='"+SARpath+"';\n")
datafile.write("$DBhost='"+DBhost+"';\n")
datafile.write("$DBname='"+DBname+"';\n")
datafile.write("$DBtable='"+DBtable+"';\n")
datafile.write("$SQLite3='"+SQLite3+"';\n")
datafile.write("$DBuser='"+DBuser+"';\n")
datafile.write("$DBpasswd='"+DBpasswd.decode()+"';\n")
datafile.write("$DBuserread='"+DBuserread+"';\n")
datafile.write("$DBpasswdread='"+DBpasswdread.decode()+"';\n")
datafile.write("$SWSserver='"+SWSserver+"' ;\n")
datafile.write("$MySQL="+MySQLtext+";\n")
datafile.write("?> \n")
datafile.close()
os.system("chmod 740 config.*")
os.system("chown :www-data config.*")

