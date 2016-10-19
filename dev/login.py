#!/usr/bin/python3
import paramiko
import getpass 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
HOST = str(input('Host IP: '))
USER = str(input('User ID: '))
PASS = getpass.getpass('Password: ')
ssh.connect(HOST, username=USER, password=PASS)

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("uptime")
output = ssh_stdout.readlines()
print (output)
