#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tsilivisn
#
# Created:     28/01/2014
# Copyright:   (c) tsilivisn 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pygmail import pygmail

g = pygmail()
g.login('nick.tsilivis@gmail.com', 'notorious3')

print g.response

g.get_mailboxes()
for item in g.mailboxes:
    print item

print(g.get_mail_count())

print(g.get_unread_count("INBOX"))

id_list = g.get_mails_from("tsilivism")

for mail in id_list:
    print(g.get_mail_from_id(mail))

g.logout()