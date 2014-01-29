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
from email.parser import HeaderParser

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

    def send_email(self, sender, to, subject, body,):

        sender = 'nick.tsilivis@gmail.com'
        to = 'nick.tsilivis@gmail.com'
        subject = 'Gmail SMTP Test'
        body = 'blah blah blah'

        "Sends an e-mail to the specified recipient."

        body = "" + body + ""

        headers = ["From: " + sender,
                   "Subject: " + subject,
                   "To: " + to,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]

        headers = "\r\n".join(headers)

        sesion = smtplib.SMTP('smtp.gmail.com', 587)

        sesion.ehlo()
        sesion.starttls()
        sesion.ehlo()
##        self.login(sender, self.password)
        self.login('nick.tsilivis@gmail.com', 'notorious3')

        sesion.sendmail(sender, to, headers + "\r\n\r\n" + body)
        sesion.quit()





