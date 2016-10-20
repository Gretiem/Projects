#!/usr/bin/python3

password = ('1234')


#attempt = str(input('Password: '))
"""
if attempt == password:
    print ('you win')
else:
    print ('you lose')
"""


while True:
    n = str(input('Password: '))
    if n.strip() == password:
        print ('correct')
        break
