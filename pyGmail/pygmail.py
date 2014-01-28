#-------------------------------------------------------------------------------
# Name:        pygmail
# Purpose:     sending email with python and gmail
#
# Author:      Nick Tsilivis
#
# Created:     28/01/2014
# Copyright:   (c) tsili852 2014
#-------------------------------------------------------------------------------

import imaplib

class pygmail:

    def __init__(self):
        self.IMAP_SERVER = 'imap.gmail.com'
        self.IMAP_PORT = 993
        self.M = None
        self.response = None
        self.mailboxes = []

    def login(self, username, password):
        self.M = imaplib.IMAP4_SSL(self.IMAP_SERVER, self.IMAP_PORT)
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

    def delete_mailbox(set, mailbox):
        rc, response = self.M.delete(mailbox)
        return rc