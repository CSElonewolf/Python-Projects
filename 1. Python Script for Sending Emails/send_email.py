
import smtplib 
import os 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart

# login credentials 
username = os.environ.get('SEND_EMAIL')
password = os.environ.get('SEND_PASS')

def send_email(
	text_body = 'Default Email Body',
	subject = 'Hello Subject',
	from_email = 'PyMail By Dev<aabc62840@gmail.com>',
	to_emails = None
	):

# checks whether "to_emails" is a "list"
	assert isinstance(to_emails,list)

# building the message_string 
	msg = MIMEMultipart('alternative')
	msg['From'] = from_email
	msg['To'] = ",".join(to_emails)
	msg['Subject'] = subject


# sending "html" version of the message body 
	text_body_part = MIMEText(text_body,'html')
	msg.attach(text_body_part)

# combining the message components
	msg_str = msg.as_string()

# login to smtp server 
	server = smtplib.SMTP(
		host='smtp.gmail.com',
		port=587
		)
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(from_email,to_emails,msg_str)

# closing the server
	server.quit()

