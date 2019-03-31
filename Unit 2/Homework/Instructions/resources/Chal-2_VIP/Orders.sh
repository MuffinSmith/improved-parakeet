#!/bin/bash
mkdir AllRecords

#Find all csv files and copy them to AllRecords
find . -type f -name "*.csv*" -exec cp -t AllRecords '{}' \;

#Find each instance of specific names and output it to file
grep -n -e "Michael,Davis" AllRecords/* >> michael_davis_orders.output
grep -n -e "Michael,Campbell" AllRecords/* >> michael_campbell_orders.output

mkdir AllRecords/VIPCustomerOrders
mv michael_campbell_orders.output AllRecords/VIPCustomerOrders/michael_campbell_orders.output
mv michael_davis_orders.output AllRecords/VIPCustomerOrders/michael_davis_orders.output

touch VIPCustomerDetails.md

#print how many records of each customer
printf "Michael Davis: " >>VIPCustomerDetails.md
cat AllRecords/VIPCustomerOrders/michael_davis_orders.output |wc -l  >> VIPCustomerDetails.md

printf " Michael Campbell: " >>VIPCustomerDetails.md 
cat AllRecords/VIPCustomerOrders/michael_campbell_orders.output |wc -l  >> VIPCustomerDetails.md
