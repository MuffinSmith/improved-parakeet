#!/bin/bash

ip="8.8.8.8"
ping -c 1 $ip > /dev/null 2>&1 && echo "$ip is up!" || echo "$ip is down!"