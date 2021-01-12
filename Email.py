#!/usr/bin/env python
# coding: utf-8

# # Sending mail using python

# In[1]:


get_ipython().system('pip install emails')


# In[ ]:


# demouse421@gmail.com and sending to temp mail


# In[3]:


import emails


# In[21]:


html_text = '''<p><span style="font-family: Courier New, courier;"><strong><span style="color: rgb(44, 130, 201);">Hi,&nbsp;,</span></strong></span></p>
<p><span style="font-family: Courier New, courier;"><strong><span style="color: rgb(44, 130, 201);">This is a demo mail for email sending project using python</span></strong></span></p>
<p><span style="font-family: Courier New, courier;"><strong><span style="font-size: 20px; color: rgb(44, 130, 201);">from,</span></strong></span></p>
<p><strong><span style="font-size: 18px; color: rgb(44, 130, 201);">DEMO</span></strong></p>'''


message = emails.html(html=html_text,
                          subject="EMAIL FROM PYTHON SCRIPT",
                          mail_from=('Demo', 'demouse421@gmail.com'))


# In[22]:


mail_via_python = message.send(to='hinoj92731@vy89.com', 
                               smtp={'host': 'smtp.gmail.com', 
                                     'timeout': 5,
                                    'port':587,
                                    'user':'demouse421@gmail.com',
                                    'password':'demoacc@421',
                                    'tls':True})


# In[23]:


mail_via_python


# In[24]:


mail_via_python.status_code


# # using function

# In[26]:


def sendMail(email,name):
    
    html_text = '''<p><span style="font-family: Courier New, courier;"><strong><span style="color: rgb(44, 130, 201);">Hi '''+name+''', &nbsp;</span></strong></span></p>
<p><span style="font-family: Courier New, courier;"><strong><span style="color: rgb(44, 130, 201);">This is a demo mail for email sending project using python</span></strong></span></p>
<p><span style="font-family: Courier New, courier;"><strong><span style="font-size: 20px; color: rgb(44, 130, 201);">from,</span></strong></span></p>
<p><strong><span style="font-size: 18px; color: rgb(44, 130, 201);">DEMO</span></strong></p>'''

    subject = "Hi,"+ name +" you have mail for Demo Testing"
    message = emails.html(html=html_text,
                          subject=subject,
                          mail_from=('Demo', 'demouse421@gmail.com'))

    
    mail_via_python = message.send(to=email, 
                               smtp={'host': 'smtp.gmail.com', 
                                     'timeout': 5,
                                    'port':587,
                                    'user':'demouse421@gmail.com',
                                    'password':'demoacc@421',
                                    'tls':True})
    return mail_via_python.status_code


# In[27]:


sendMail("hinoj92731@vy89.com","Hino")


# In[ ]:




