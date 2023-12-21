import tkinter as tk
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

window = tk.Tk()
window.title('f0cus Mail Sender')
window.geometry("500x500")

def attach_file():
    file = filedialog.askopenfilename()

    if file:
        attachment_label.config(text=f"Selected File: {file}")
def mail_send():
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = entry1.get()
    password = entry2.get()
    message_body = entry4.get()
    message_subject = entry5.get()

    with open('mail_list.txt', 'r') as file:
        recipients = [line.strip() for line in file if line.strip()]

    for recipient_email in recipients:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = message_subject

        message.attach(MIMEText(message_body, 'plain'))


        if 'dosya_yolu' in globals():
            with open(attach_file, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {attach_file}',
                )
                message.attach(part)

        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, message.as_string())
                print(f'Email {recipient_email} successfully sent to!')
        except smtplib.SMTPAuthenticationError:
            print('Error: Authentication failed.')

label1 = tk.Label(window, text='Please enter your user email:')
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text='Please enter your user password:')
label2.pack()

entry2 = tk.Entry(window, show="*")
entry2.pack()

attachment_button = tk.Button(window, text="Add file", command=attach_file)
attachment_button.pack()

attachment_label = tk.Label(window, text="Selected File: ")
attachment_label.pack()

label4 = tk.Label(window, text='Please enter your e-mail message:')
label4.pack()

entry4 = tk.Entry(window)
entry4.pack()

label5 = tk.Label(window, text='Please enter the email title:')
label5.pack()

entry5 = tk.Entry(window)
entry5.pack()

send_button = tk.Button(window, text="Send", command=mail_send)
send_button.pack()

window.mainloop()
