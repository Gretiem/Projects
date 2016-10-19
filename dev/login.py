#!/usr/bin/python3

import subprocess
import sys
import getpass

HOST = str(input('Host IP: '))
PW = getpass.getpass('Password: ')
USER = ('') #inset user log in here when using
COMMAND="/bin/echo %s | uname -a" % PW
#ssh = subprocess.Popen(["ssh", "-l", USER, "-t", "%s" % HOST, PW, COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ssh = subprocess.Popen(["ssh", "-l", USER, "-t", "%s" % HOST, PW, COMMAND], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result = ssh.stdout.readlines()
if result == []:
	error = ssh.stderr.readlines()
	print >>sys.stderr, "ERROR: %s" % error
else:
	print (result)
