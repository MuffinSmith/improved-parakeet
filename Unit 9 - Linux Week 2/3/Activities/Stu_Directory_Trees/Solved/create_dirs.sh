#!/bin/bash

# Create a new directory, called Cybersecurity
mkdir Cybersecurity

# Move into the new directory
cd Cybersecurity

# Create directories: Unit_1/1; Unit_1/2; Unit_1/3; Unit_2/1; etc.
for UNIT in $(seq 1 24)
do
  mkdir -p Unit_$UNIT/{1,2,3}
done
