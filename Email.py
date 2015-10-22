from os.path import expanduser
from os import listdir
import fnmatch


__author__ = 'Dan'

class Email:

    def email(self):
        home = expanduser("~")
        for file in listdir(home):
            if fnmatch.fnmatch(file, 'creds.txt'):
                lines = file.readlines()
                for line in lines:
                    index = line.index('=')
                    print(line[index:])



#TODO: http://stackoverflow.com/questions/157938/hiding-a-password-in-a-python-script
#TODO: https://docs.python.org/3.5/library/email-examples.html
#u_name
#p_word