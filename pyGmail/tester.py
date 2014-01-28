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
import pygmail

g = pygmail()
g.login('nick.tsilivis@gmail.com', 'notorious3')

print g.response


