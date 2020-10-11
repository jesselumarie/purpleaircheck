from lib import email, message


recipients = []

message, subject = message.get_text()

email.send_email(message, subject, recipients)

