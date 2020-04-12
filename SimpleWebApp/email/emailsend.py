import smtplib

from email.message import EmailMessage

email_content = '''Dear Sir/Madam,

This is test email.

Thanks
XXXXX'''


email = EmailMessage()

email['Subject'] = 'This is Test email'
email['From'] = 'test@gmail.com'
email['To'] = 'test@gmail.com'

email.set_content(email_content)

smtp_connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connection.starttls()
smtp_connection.login('test@gmail.com','password')

smtp_connection.send_message(email)
smtp_connection.quit()
