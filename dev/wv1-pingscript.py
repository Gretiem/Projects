#!/usr/bin/python3
import subprocess 

host = str(input('IP: '))
p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)
output = p1.communicate()[0]

print (output)
