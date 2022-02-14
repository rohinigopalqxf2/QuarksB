"""
Skype conf
"""
import time
import random

SKYPE_SENDER_ENDPOINT = "https://skype-sender.qxf2.com/send-message"
MESSAGE = 'This is a test message - '+ str(time.time()) + ' '.join(random.choices(['s1', 'h2', 'i3', 'v4', 'a5']))
