SENDER = 'db_bondy@hotmail.com'


from os.path import expanduser
from os import chdir
from glob import glob
from smtplib import SMTP
from email.mime.text import MIMEText


__name__ = 'emailer'
__author__ = 'Dan'


def email():
    msg = MIMEText("This is a test message for a test email.")
    msg['Subject'] = "This is an email sent from Python!"
    msg['From'] = 'db_bondy@hotmail.com'

    creds = __obtain_creds__()

    with SMTP('smtp-mail.outlook.com', '587') as smtp:
        smtp.set_debuglevel(False)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(creds[0], creds[1])

        smtp.sendmail(SENDER, SENDER, msg.as_string())

# TODO pull SMTP settings from creds.txt, rather than bake them in.

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
            u_name = __strip_value__(lines[0])
            p_word = __strip_value__(lines[1])

            return u_name, p_word
    else:
        error = 'No Credentials file found in {0}'.format(home)
        raise OSError(error)


# TODO: https://docs.python.org/3.5/library/email-examples.html
