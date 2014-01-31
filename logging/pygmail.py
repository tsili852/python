#-------------------------------------------------------------------------------
# Name:        pygmail
# Purpose:     sending email with python and gmail
#
# Author:      Nick Tsilivis
#
# Created:     28/01/2014
# Copyright:   (c) tsili852 2014
#-------------------------------------------------------------------------------

import imaplib, re, smtplib
import os, re
import sys
from email.parser import HeaderParser
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class pygmail:
    def __init__(self):
        self.IMAP_SERVER = 'imap.gmail.com'
        self.IMAP_PORT = 993
        self.M = None
        self.response = None
        self.mailboxes = []
        self.password = None

        self.SMTP_SERVER = 'smtp.gmail.com'
        self.SMTP_PORT = 587

    def login(self, username, password):
        self.M = imaplib.IMAP4_SSL(self.IMAP_SERVER, self.IMAP_PORT)
        self.password = password
        rc, self.response = self.M.login(username, password)
        return rc

    def logout(self):
        self.M.logout()

    def get_mailboxes(self):
        rc, self.response = self.M.list()
        for item in self.response:
            self.mailboxes.append(item.split('/', 1)[-1])
        return rc

    def rename_mailbox(self, oldmailbox, newmailbox):
        rc, response = self.M.rename(oldmailbox,newmailbox)
        return rc

    def create_mailbox(self, mailbox):
        rc, self.response = self.M.create(mailbox)
        return rc

    def delete_mailbox(self, mailbox):
        rc, response = self.M.delete(mailbox)
        return rc

    def get_mail_count(self, folder='Inbox'):
        rc, count = self.M.select(folder)
        return count[0]

#   MESSAGES - The number of messages in the mailbox.
#   RECENT - The number of messages with the Recent flag set.
#   UIDNEXT - The next unique identifier value of the mailbox.
#   UIDVALIDITY - The unique identifier validity value of the mailbox.
#   UNSEEN - The number of messages which do not have the Seen flag set. """

    def get_unread_count(self, folder):
        rc, message = self.M.status(folder, "(UNSEEN)")
        unreadCount = re.search("UNSEEN (\d+)", message[0]).group(1)
        return unreadCount


    def get_mail_headers():
        resp, data = M.FETCH(1, '(RFC822')
        msg = HeaderParser().parsestr(data[0][1])
        return msg['From'], msg['To'], msg['Subject']



    def get_mails_from(self, uid, folder='Inbox'):
        status, count = self.M.select(folder, readonly=1)
        status, response = self.M.search(None, 'FROM', uid)
        email_ids = [e_id for e_id in response[0].split()]
        return email_ids

    def get_mail_from_id(self, id):
        status, response = self.M.fetch(id, '(body[header.fields (subject)])')
        return response

    def send_email(self, sender, recipient, subject, body):

        body = "" + body + ""

        headers = ["From: " + sender,
                   "Subject: " + subject,
                   "To: " + recipient,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        session = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)

        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(sender, self.password)

        session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
        session.quit()

    def send_email_with_attachmen(self, sender, recipient, subject, directory, fileName):
        '''filename = file with extention
           The attachment will be sent according to the extention - for images only .jpg
           If you want to send all pictures inside the directory put only the extention on the fileName'''

        extension = os.path.splitext(fileName)[1][1:]

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['To'] = recipient
        msg['From'] = sender

        if (extension == ".jpg") :
            files = os.listdir(directory)
            imgsearch = re.compile(".jpg", re.IGNORECASE)
            files = filter(imgsearch.search, files)
            for filename in files:
                path = os.path.join(directory, filename)
                if not os.path.isfile(path):
                    continue

                img = MIMEImage(open(path, 'rb').read(), _subtype="jpg")
                img.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(img)
        else :
            part = MIMEApplication(open(directory + fileName,"rb").read())
            part.add_header('Content-Disposition', 'attachment', filename=fileName)
            msg.attach(part)

        session = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)

        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(sender, self.password)

        session.sendmail(sender, recipient, msg.as_string())
        session.quit()



