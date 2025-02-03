class notification:
    def send():
        pass
class EmailNotification():
    def send(self):
        print("Email Notification")
class SMSNotification():
    def send(self):
        print("sms")
        
s=SMSNotification()
s.send()
e=EmailNotification()
e.send()