# import sched, time

# scheduler = sched.scheduler(time.time, time.sleep)

# def print_event(name):
#     print('EVENT:', time.time(), name)

# print('START:', time.time())
# scheduler.enter(2, 1, print_event, ('first',))
# scheduler.enter(3, 1, print_event, ('second',))

# scheduler.run()


# import smtplib
# from email.message import EmailMessage

# def send_email(subject, body):
#     msg = EmailMessage()
#     msg.set_content(body)
#     msg['Subject'] = subject
#     msg['From'] = 'willmorris188@gmail.com'
#     msg['To'] = 'willmorris103@gmail.com'

#     # Establish a connection to your email server. This example uses Gmail.
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login('willmorris188', 'eiyazspjuqpfflru')
#     server.send_message(msg)
#     server.quit()

# send_email('Hello', 'How are you?\n this is a test')

