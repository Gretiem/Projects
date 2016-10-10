#!/usr/bin/python3
import subprocess
import sys
from sys import stdout
pw = str('1234')

#subprocess.call(['./pwcheck.py'])
output = subprocess.check_output(['./pwcheck.py'], stderr=stdout, timeout=120)


#attempt at trying an if statement
"""
subprocess.call(['./pwcheck.py'])

if sys.argv == 'Password: ':
    print ('1234')
else:
    print ('it broke')
"""

"""
jank = str(input('username: '))
#subprocess.call(['echo', jank])

output = subprocess.check_output(['echo', jank])
print (output)
"""


#output = subprocess.check_output(['{0}'.format(c3)])

#works
#command = ('ls')
#output = subprocess.check_output(['{0}'.format(command)])

#Standard use of command
#output = subprocess.check_output(['ls', '-al'])

#print ('Have %d bytes in output' % len(output))
#print (output)

