#!/bin/bash
#Name,Email,Password,Phone,Address,City,Zip,Country,CC,CVV,Balance

import csv
import hashlib

encoding = 'utf-8'

with open('/home/muffin/Repos/improved-parakeet/Unit 5/HW/Instructions/Resources/UserInfo.csv','rt',encoding=encoding, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    with open('/home/muffin/Repos/improved-parakeet/Unit 5/HW/Instructions/Resources/Hashes.csv', 'wt',encoding=encoding, newline='') as hashfile:
        csvwriter=csv.DictWriter(hashfile, csvreader.fieldnames)
        csvwriter.writeheader()
        for row in csvreader:
            #TODO hash passwords and cc#s
            #this spits out a list and index 2 and 8 need to be hashed
            sha256 = hashlib.sha256()
            sha256.update(row['Password'].encode(encoding))
            row['Password'] = sha256.hexdigest()
            sha256 = hashlib.sha256()
            sha256.update(row['CC'].encode(encoding))
            row['CC'] = sha256.hexdigest()
            csvwriter.writerow(row)

            
            

