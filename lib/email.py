import smtplib, ssl

# Here are the email package modules we'll need
from email.message import EmailMessage
from datetime import date

username = 'foo'
password = 'bar'

def send_email(message, subject, recipients):
    for recipient in recipients:
        # Create the container email message.
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From']=f'{username}@gmail.com'
        msg['To'] = recipient
        msg.set_content(message)

        try:
            smtp_server = "smtp.gmail.com"
            port = 587  # For starttls
            context = ssl.create_default_context()
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(username, password)

            print(message)
            # server.send_message(msg)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()

