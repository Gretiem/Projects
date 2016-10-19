#!/usr/bin/python3

import subprocess
import sys
import getpass

HOST = str(input('Host IP: '))
PW = getpass.getpass('Password: ')
USER = ('') #inset user log in here when using
COMMAND="/bin/echo %s | uname -a" % PW
#ssh = subprocess.Popen(["ssh", "-l", USER, "-t", "%s" % HOST, PW, COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
"""
#working block 1 - ssh's to box, doesn't enter password
ssh = subprocess.Popen(["ssh", "-l", USER, "-t", "%s" % HOST, PW, COMMAND], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result = ssh.stdout.communicate()
# if below is removed it will still ask to log in. 
if result == []:
	error = ssh.stderr.readlines()
	print >>sys.stderr, "ERROR: %s" % error
else:
	print (result)
"""

TRY = 
ssh = subprocess.Popen(["ssh", "-l", USER, "-t", "%s" % HOST, "%s" % TRY], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
result = ssh.stdout.check_output()
if result == "carter@153.82.36.202's password:":
	ssh.stdin.communicate(PW)
#login = ssh.stdin.communicate(str(PW))

print (login)

