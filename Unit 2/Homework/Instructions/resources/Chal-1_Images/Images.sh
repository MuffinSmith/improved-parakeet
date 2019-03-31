#!/bin/bash
unzip -o Pictures.zip
mkdir JPG
#Finds and moves each file to the correct folder based on file type
find . -name "*.jpg" -exec mv -t JPG '{}' \;

mkdir PNG
find . -name "*.png" -exec mv -t PNG '{}' \;

mkdir TIFF
find . -name "*.tiff" -exec mv -t TIFF '{}' \;

rm -r Pictures

#finds each file then takes the output and strips it of everything but the extention,
#Sorts the output, counts how many of each repeating string there is, 
#Then strips everythin but the three file types I want and outputs it to a file.
find . -type f | sed -e 's/.*\.//' | sort | uniq -c | grep -Ei '(tiff|jpg|png)$' >> PictureCounts.md
