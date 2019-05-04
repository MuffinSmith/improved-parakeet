#!/bin/bash

# 1. Print "Moe", "Larry", and "Curly"
for NAME in "Moe" "Larry" "Curly"
do
  echo "$NAME"
done

# 2. Print "I've used Mac OSX"; "I've used Windows"; and "I've used Linux"
for OPERATING_SYSTEM in "Mac OS X" "Windows" "Linux"
do
  echo "I've used $OPERATING_SYSTEM."
done

# 3. You do NOT need to change this block. Just run it. Then, answer: What does `*` mean?
for FILE in *
do
  echo "$FILE"
done

# 4. Run: `seq 1 10`. What does this print?
# SOLUTION: It prints the numbers from 1 to 10.
seq 1 10

# 5. Use command expansion and `seq` to print every number between 1 and 24.
for NUMBER in $(seq 1 24)
do
  echo $NUMBER
done
