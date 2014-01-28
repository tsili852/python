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
g.login('basementproject.gr@gmail.com', 'notorious3')

print g.response

g.get_mailboxes()
for item in g.mailboxes:
    print item