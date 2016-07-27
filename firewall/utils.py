import os
import sys
import logging

from functools import wraps
from subprocess import Popen, PIPE

from constants import DEBUG, OS_TYPE

import time


class Die(Exception):
    def __init__(self, msg=None):
        Exception.__init__(self)
        self.msg = msg


class RunCMD(object):
    """
    TODO: make a better progress bar
          better exceptions
    """
    def __call__(self, cmd):
        self.run = Popen(cmd, shell=True, stdout=PIPE)
        try:
            if DEBUG:
                for line in iter(self.run.stdout.read, ''):
                    print line.rstrip()
            else:
                while self.run.poll() is None:
                    time.sleep(1)
                    print "\b.",
                    sys.stdout.flush()

        except:
            raise Die("Error during command")

    def __del__(self):
        print "finished"
        self.run.stdout.close()


def mylogger(fn):
    logging.basicConfig(filename='{}.log'.format(format(fn.__name__)), level=logging.INFO)

    @wraps(fn)
    def wrapper(*args, **kwargs):
        logging.info(
            'ran with args: {}, and kwargs: {}'.format(args, kwargs)
        )
        return fn(*args, **kwargs)
    return wrapper


class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """

    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)


