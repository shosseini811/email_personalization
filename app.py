import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
email = 'your-email@gmail.com'
password = 'your app-specific password'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# List of recipients with their names
recipients = [
    {'name': 'Person1', 'email': 'person1@example.com'},
    {'name': 'Person2', 'email': 'person2@example.com'}
]

# Login to the email server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email, password)

# Sending email to each recipient
for recipient in recipients:
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient['email']
    msg['Subject'] = 'Your Subject Here'
    
    # Personalize the email message
    body = f"""Hello {recipient['name']},

    I hope this email finds you well...

    Best regards,
    Your Name"""
    msg.attach(MIMEText(body, 'plain'))
    
    # Send the email
    server.sendmail(email, recipient['email'], msg.as_string())

# Quit the server
server.quit()