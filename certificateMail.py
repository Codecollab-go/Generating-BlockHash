import datetime
import hashlib
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# define the email addresses and credentials
sender_email = 'rehansharma9917@gmail.com'
sender_password = 'Aryan@9917'
recipient_email = '0201csai038@niet.co.in'

# define the certificate data
name = "John Doe"
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# create a hash of the certificate data using SHA-256
certificate_data = f"{name}{date}".encode('utf-8')
certificate_hash = hashlib.sha256(certificate_data).hexdigest()

# define the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'Certificate'

# add a text message to the email
text = f"Dear recipient, please find attached your certificate. \nCertificate hash: {certificate_hash}"
msg.attach(MIMEText(text))

# add the certificate file as an attachment to the email
certificate_filename = 'certificate.txt'
with open(certificate_filename, 'w') as f:
    f.write(f"Name: {name}\nDate: {date}\nHash: {certificate_hash}")
with open(certificate_filename, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='txt')
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(certificate_filename))
    msg.attach(attachment)

# send the email using the Gmail SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())




# In this code, we first define the email addresses and credentials for the sender 
# and recipient.

# We then generate a certificate as we did in the earlier example code and store the 
# certificate data in a text file named certificate.txt.

# Next, we define the email message using the MIMEMultipart class, and we add a text 
# message to the email using the MIMEText class. We then add the certificate file as 
# an attachment to the email using the MIMEApplication class.

# Finally, we use the smtplib.SMTP_SSL class to connect to the Gmail SMTP server and 
# send the email using the server.sendmail() method.

# Note that you will need to enable the "Less secure app access" option in your 
# Gmail account settings to use this code. Alternatively, you can use a different 
# email provider or email API to send the email.



