#!/usr/bin/env python
# coding: utf-8

# In[1]:


from string import Template

# import the smtplib module. It should be included in Python by default
import smtplib

# import necessary packages for MIME
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# In[2]:


#Global field declaration
smtp_host = 'smtp.gmail.com'
smtp_port = 25
team_foodie_email = 'FoodieHimAmar@gmail.com'
team_foodie_pwd = 'HimAmar@007'
email_subject = 'List of top 5 restaurants for your hunger'
msg_success = 'Mail sent to the email. Have a good day.'
msg_failure = 'Sorry,  we are unable to send the mail. Please try again in sometime.'


# In[3]:


def set_up_email_server(cust_email):
# set up the SMTP server
    smtp_server = smtplib.SMTP(host= smtp_host, port=smtp_port)
    smtp_server.starttls()
    smtp_server.login(team_foodie_email, team_foodie_pwd)
    return smtp_server


# In[4]:


def trigger_email(smtp_server, cust_email, message):
    
    msg = MIMEMultipart()       # create a message
    
    # setup the parameters of the message
    msg['From']= team_foodie_email
    msg['To']= cust_email
    msg['Subject']= email_subject
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    smtp_server.send_message(msg)
    del msg


# In[5]:


def close_email_server_connection(smtp_server):
    smtp_server.quit()


# In[6]:


def prepare_message(cust_name, restaurants):
    greet_template = Template('Dear ${Customer},\n\n')
    rest_template = Template('${restaurant_name} in ${restaurant_address} has been rated ${rating}.\n')
    messages = []
    messages = greet_template.substitute(Customer = cust_name)
    for rest in restaurants:
        messages.append(rest_template.substitute(restaurant_name = rest[restaurant_name], 
                                                 restaurant_address = rest[restaurant_address], rating = rest[rating]))
    messages.append('\nKind Regards,\nTeam Foodie')
    final_messgae = ''.join(messages)
    
    return final_message


# In[7]:


def send_email(cust_name, cust_email, restaurants):

    final_message = prepare_message(cust_name, restaurants)
    
    try:
        smtp_server = set_up_email_server(cust_email)
    except:
        return msg_failure
    
    try:
        trigger_email(smtp_server, cust_email, final_message)
    except:
        return msg_failure
    
    close_email_server_connection(smtp_server)

    return msg_success
    
        

