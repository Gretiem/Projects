#!/usr/bin/python3
import paramiko
import getpass 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
HOST = str(input('Host IP: '))
USER = str(input('User ID: '))
PASS = getpass.getpass('Password: ')
PORT = 22
ssh.connect(HOST, port=PORT, username=USER, password=PASS)


#each command will be run befor logging out of the device.  
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("uptime")
output = ssh_stdout.readlines()
print (output)

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("uname")
output = ssh_stdout.readlines()
print (output)



