#!/usr/bin/python3
import paramiko
import getpass 

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#Have these as variables to help thos viewing this code see where the variables belong.
#Am trying to add multi commands, then have them write to a file

HOST = str(input('Host IP: '))
USER = str(input('User ID: '))
PASS = getpass.getpass('Password: ')


ssh.connect(HOST, username=USER, password=PASS)

remote_conn = ssh.invoke_shell()
output = remote_conn.recv(65535)
print (output)

remote_conn.send("\nuptime\n")
output = remote_conn.recv(65535)
print (output)


remote_conn.send("uname")
output = remote_conn.recv(65535)
print (output)

