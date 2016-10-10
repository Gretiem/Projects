#!/usr/bin/python3
import subprocess


jank = str(input('username: '))
#subprocess.call(['echo', jank])






output = subprocess.check_output(['echo', jank])
print (output)

#output = subprocess.check_output(['{0}'.format(c3)])

#works
#command = ('ls')
#output = subprocess.check_output(['{0}'.format(command)])

#Standard use of command
#output = subprocess.check_output(['ls', '-al'])

#print ('Have %d bytes in output' % len(output))
#print (output)
