#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib


# In[ ]:


server = smtplib.SMTP('smtp.gmail.com', 587)


# In[ ]:


server.starttls()


# In[ ]:


server.login("rishabhkhandelwal96499@gmail.com","9649939246")


# In[ ]:


message = "Congratulations... You got training model accuracy as desired."


# In[ ]:


server.sendmail('rishabhkhandelwal96499@gmail.com','rishabhkhandelwal96499@gmail.com', message)


# In[ ]:


server.quit()

