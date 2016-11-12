#!/usr/bin/python3 
import getpass
import subprocess

PASS = getpass.getpass('Pass: ')

subprocess.call(['sudo', 'uptime'])
subprocess.call([PASS, '\n'])
