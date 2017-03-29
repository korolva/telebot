#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import paramiko
import time
from random import choice
import string

login = sys.argv[1]



def adduser(x):
   host = '172.17.2.104'
   user = ''
   sudopass = ''
   port = 22
   password = ''.join(choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10))
   client = paramiko.SSHClient()
   client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   client.connect(hostname=host, username=user, port=port,)
   stdin, stdout, stderr = client.exec_command('sudo chown v.korol:v.korol /etc/freeradius/users', get_pty=True)
   stdin.write(sudopass)
   stdin.flush()
   time.sleep(2)
   stdin, stdout, stderr = client.exec_command('echo ' + x + ' Cleartext-Password := ' + password + '>> /etc/freeradius/users')
   stdin, stdout, stderr = client.exec_command('sudo chown root:root /etc/freeradius/users', get_pty=True)
   stdin.write(sudopass)
   stdin.flush()
   data = stdout.read() + stderr.read()
   client.close()
   print('user:' + x + '\n' + 'password:' + password)

adduser(login)
