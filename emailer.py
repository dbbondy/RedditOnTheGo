from os.path import expanduser
from os import listdir
import fnmatch

__name__ = 'emailer'
__author__ = 'Dan'


def email():
    home = expanduser("~")
    for file in listdir(home):
        if fnmatch.fnmatch(file, 'creds.txt'):
            lines = file.readlines()
            for line in lines:
                index = line.index('=') + 1
                print(line[index:])


#TODO: http://stackoverflow.com/questions/157938/hiding-a-password-in-a-python-script
#TODO: https://docs.python.org/3.5/library/email-examples.html
#u_name
#p_word