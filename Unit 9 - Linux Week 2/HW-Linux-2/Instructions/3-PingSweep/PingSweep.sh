#!/bin/bash
PREFIX=$1
echo "Scanning $PREFIX.0/24..."
for SEQUENCE in $(seq 0 5)
	do TARGET=$PREFIX.$SEQUENCE
	ping -c 1 -w 1 $TARGET 1> /dev/null 2> /dev/null
	RESULT=$?
	if [ $RESULT -eq 0 ]
	then
		echo "$TARGET is UP" >> live_hosts
	else
		echo "$TARGET is DOWN" >> down_hosts
	fi
done
cat down_hosts
cat live_hosts