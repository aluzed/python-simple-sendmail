# Example from : https://docs.python.org/2/library/email-examples.html

# get our config
from config import *

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

textfile = 'mail.txt'

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = 'Test Melberries'
msg['To'] = 'Dest <jane.doe@domain.com>'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP(smtpCfg)
s.starttls()
s.login(mailCfg['login'], mailCfg['pwd'])
s.sendmail(mailCfg['login'], ['jane.doe@domain.com'], msg.as_string())
s.quit()
