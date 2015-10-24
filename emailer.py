from os.path import expanduser
from os import chdir
from glob import glob
from smtplib import SMTP
from email.mime.text import MIMEText

SENDER = 'db_bondy@hotmail.com'

__name__ = 'emailer'
__author__ = 'Dan'


def email():
    msg = MIMEText("This is a test message for a test email.")
    msg['Subject'] = "This is an email sent from Python!"
    msg['From'] = 'db_bondy@hotmail.com'

    creds = __obtain_creds__()

    smtp_addr = creds['smtp']
    smtp_port = creds['smtp_port']

    with SMTP(smtp_addr, smtp_port) as smtp:
        smtp.set_debuglevel(False)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        username = creds['u_name']
        password = creds['p_word']
        smtp.login(username, password)

        smtp.sendmail(SENDER, SENDER, msg.as_string())


def __strip_value__(line):
    index = line.index('=') + 1
    return line[index:]


def __obtain_creds__():
    home = expanduser("~")

    chdir(home)
    creds_file = glob('creds.txt')
    if creds_file:
        with open(creds_file[0]) as file:
            lines = file.read().splitlines()
            smtp = __strip_value__(lines[0])
            smtp_port = __strip_value__(lines[1])
            u_name = __strip_value__(lines[2])
            p_word = __strip_value__(lines[3])

            creds = {'smtp' : smtp, 'smtp_port' : smtp_port, 'u_name': u_name, 'p_word' : p_word}

            return creds
    else:
        error = 'No Credentials file found in {0}'.format(home)
        raise OSError(error)

# TODO: https://docs.python.org/3.5/library/email-examples.html
