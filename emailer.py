from os.path import expanduser
from os import listdir
from os import chdir
from glob import glob

__name__ = 'emailer'
__author__ = 'Dan'


def email():
    pass


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
