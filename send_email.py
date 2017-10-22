
#send_email function
def send_email(user,pwd,recipient,subject,body):
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    msg = MIMEMultipart()
    msg['FROM'] = user
    msg['TO'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(user, recipient, text)
    server.quit()

#User specified parameters
user = 'user@gmail.com'
pwd = 'password'
recipient = 'to@gmail.com'
subject = 'Bitcoin_update'
body = '''Daily update - Bitcoin'''

#Use the send_email function
send_email(user,pwd,recipient,subject,body)
