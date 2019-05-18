#!/bin/bash

for USER in $(cat usernames.txt); do
  id $USER > /dev/null 2>&1 && echo "$USER exists!"
done
