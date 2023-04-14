import email
import imaplib

# set up IMAP connection

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('user-emailaddress', 'password')
mail.select('inbox')

# search for emails containing the keyword 'free' in subject or body
typ, data = mail.search(None, '(OR SUBJECT "free" BODY "free")')

# move matched emails to spam folder
for num in data[0].split():
    mail.store(num, '+X-GM-LABELS', '\\Spam')
    mail.store(num, '+FLAGS', '\\Deleted')

mail.expunge()
mail.close()
mail.logout()
