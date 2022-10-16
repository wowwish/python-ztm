#################################################################################################################
# DONOT SAVE YOUR EMAIL SCRIPTS IN PYTHON AS 'email.py'. IT WILL RAISE ERRORS!!!!!                              #
# YOU NEED TO ALLOW ACCESS TO LESS SECURE APPS FROM YOUR ACCOUNT SETTINGS IN GMAIL FOR THIS SCRIPT TO WORK!!!!  #
# USE A DUMMY GMAIL ACCOUNT AS THE RECIPIENT AND DONOT USE PERSONAL OR PROFESSIONAL ACCOUNTS!!!                 #
#################################################################################################################

import smtplib # package for SMTP (Simple Mail Transfer Protocol) communication protocol used to setup SMTP server
from email.message import EmailMessage # In-built python package for sending emails
from string import Template # to help us substitute variables inside of text in the template HTML
# GOOD PRACTICE: ALWAYS USE pathlib's Path OBJECTS TO WORK WITH FILES AND DIRECTORIES WHEN POSSIBLE
from pathlib import Path # to read the HTML template file

html = Template(Path('email_template.html').read_text()) # use the read_text() method of a Path object to read 
# file content as text and create a Template object out of it for substituting variables inside of the text

email = EmailMessage() # Initiate the email object
email['from'] = 'Dio Brando' # The person sending the mail
email['to'] = '<recipient address>' # The email-address to send the mail. Make this a list of email-addresses
# to send to multiple recipients.
email['subject'] = 'You won a million $Dollars$!' # email subject
# The email Content
# substitute variable '$name' inside of the HTML content (text form)
# We can also substitute multiple variables in the text content of Template object at one go using the same
# substitute() method
email.set_content(html.substitute(name='Jotaro Kujoh'), 'html') # Set the content-type as HTML instead of text
# to render it properly in the mail 

# Use SMTP server to login to the Gmail Client and send the Mail
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: # Connect to the Gmail SMTP server at 'smtp.gmail.com' 
# at the standard SMTP port 587
    smtp.ehlo() # part of SMTP protocol agreement. The client sends this command to the SMTP server to identify 
    # itself and initiate the SMTP conversation.
    # EHLO tells the server that the client may want to use the Extended SMTP (ESMTP) protocol instead. 
    # EHLO can be used although you will not use any ESMTP command. And servers that do not offer any additional 
    # ESMTP commands will normally at least recognize the EHLO command and reply in a proper way.
    smtp.starttls()
    # E-mail servers and clients that uses the SMTP protocol normally communicate using plain text over the 
    # Internet. The communication often goes through one or more routers that is not controlled or trusted by 
    # the server and client. This communication can be monitored and it is also possible to alter the messages 
    # that are sent via the routers.
    # To improve security, an encrypted TLS (Transport Layer Security) connection can be used when 
    # communicating between the e-mail server and the client. TLS is most useful when a login 
    # username and password (sent by the AUTH command) needs to be encrypted. TLS can be used to encrypt the 
    # whole e-mail message, but the command does not guarantee that the whole message will stay encrypted the 
    # whole way to the receiver; some e-mail servers can decide to send the e-mail message with no encryption. 
    # But at least the username and password used with the AUTH command will stay encrypted. Using the STARTTLS 
    # command together with the AUTH command is a very secure way to authenticate user
    smtp.login('<sender address>', '<sender password>') # Login using Credentials
    smtp.send_message(email)
    print('All Good Boss!')