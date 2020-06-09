#!/usr/bin/env python
# coding: utf-8

# In[3]:


import smtplib

gmail_user = 'rishabhkhandelwal96499@gmail.com'
gmail_password = '9649939246'

sent_from = gmail_user
to = ['rishabhkhandelwal96499@gmail.com']
subject = 'MLOps Project'
body = 'Congratulations. You got desired accuracy.'

email_text = """From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')

