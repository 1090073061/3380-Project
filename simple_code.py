# -*- coding: utf-8 -*-
"""Simple code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fd5_kFjkxitYGVC7fs_Do_cfnBVFk9pp
"""

import smtplib, ssl
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import re

class emailSender:
  smtp_server = "smtp.gmail.com"
  port = 587  # For starttls
  sender_email = "jchi6666@gmail.com"
  password = "Ww545097926"
  receiver_email = "jchi3@lsu.edu"
  message = "Testing message"
  regex = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

  def getEmail(msg):
    #extract email from a string
    if identifier(msg) = a
      return msgBuilder(a)
    if identifier(msg) = b
      return msgBuilder(b)
    if identifier(msg) = c
      return msgBuilder(c)
  
  def sendEmail(msg):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "jchi6666@gmail.com"
    password = "Ww545097926"
    receiver_email = "jchi3@lsu.edu"
    message = msg
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
      print(1)
      server = smtplib.SMTP(smtp_server,port)
      server.ehlo() # Can be omitted
      server.starttls(context=context) # Secure the connection
      server.ehlo() # Can be omitted
      server.login(sender_email, password)
      # TODO: Send email here
      server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

  def msgBuilder(x):
    #build msg according to each requirement
    if x = a
      return sendEmail('Added')
    elif  x = b
      return sendEmail('Deleted')
    elif x = c
      return sendEmail('Unknow request')

class messageIdentify:
  def identifier(x):
    a = 'add email'
    b = 'delete email'
    c = 'unknown'
    if '添加' in x or 'add' in x:
      return a
    elif 'delete' in x:
      return b
    else:
      return c

emailSender.sendEmail()