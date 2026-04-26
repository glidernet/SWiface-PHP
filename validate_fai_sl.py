#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#
#   This function validates the FAI's sporting licenses
#
# ================================================================================================================= #

import sys
import json
import urllib.request, urllib.error, urllib.parse
import datetime
import time
import os
import math
import pycountry
import socket
import config
password=config.FAIPWD
def get_licenses_per_country(country,prt=False):
   licenses=[]
   start=0
   nl=100
   while nl == 100:				# while is not over ???
      url="https://extranet.fai.org/api/v1/licences?auth_username=FAIOrganizer&auth_password="+password+"&discipline=Gliding&country="+country+"&limit_length=100&limit_start="+str(start)
      if True:
         print (url,"\n\n")
      j = urllib.request.urlopen(url)
      rr=j.read().decode('UTF-8') 
      j_obj = json.loads(rr)
      nl=len(j_obj)
   
      for lic in j_obj:
         if lic["Sport"] == 'Gliding':
            #print (lic)
            licenses.append(lic)
      if prt:
         print ("NL:", nl, "Start", start, "Lics", len(licenses))
      start += nl
   return (licenses)

def validate_fai_sl(country,sl=0, name=' ',prt=True):
    lpc=get_licenses_per_country(country, prt)
    if prt:
       print (len(lpc), sl, name, json.dumps(lpc, indent=4))
    if sl != 0:
       for lic in lpc:
           if lic['idlicencee'] == sl:
              return (True)
       return (False)
    elif name != ' ':
       for lic in lpc:
           if lic['surname_lip'].upper() == name.upper():
              return (True)
       return (False)
    else:
       return (-1)

def get_license_details_byname(country, givenname=' ', surname=' ', prt=False):
    #print("LLL->", givenname, ":::", surname)
    lpc=get_licenses_per_country(country, prt)
    if prt:
       print ("LIC:\n", len(lpc), givenname, surname, "\n\n", json.dumps(lpc, indent=4))
    for lic in lpc:
        if givenname == ' ' or givenname == '':
           if lic['surname_lip'].upper() == surname.upper() :
              return (lic)
        else: 
           if lic['surname_lip'].upper() == surname.upper() and lic['givenname_lip'].upper() == givenname.upper():
              return (lic)
    return (None)

def get_license_details_byln(country, ln, prt=True):
    lpc=get_licenses_per_country(country, prt)
    if prt:
       print (len(lpc), ln, "\n\n", json.dumps(lpc, indent=4))
    for lic in lpc:
        if lic['idlicencee'] == ln:
           return (lic)
    return (None)

def get_full_license_details(idlicence, prt=False):
    l=str(idlicence)
    url="https://extranet.fai.org/api/v1/licence/"+l+"?auth_username=FAIOrganizer&auth_password="+password
    if prt:
       print (url,"\n\n")
    j = urllib.request.urlopen(url)
    rr=j.read().decode('UTF-8') 
    j_obj = json.loads(rr)
    return(j_obj)
#################################################################
