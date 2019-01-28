import threading
import hashlib
import os
import logging
import random
import string
import sys
import time
import unittest

import os

import apiritif
from apiritif.feeders import CSVFeeder

vars = {}

data_feeder = CSVFeeder(os.path.join(os.path.dirname(__file__), "data/source.csv"), vars)


class TestSimple(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data_feeder.read_vars()

    def setUp(self):
        new_vars = data_feeder.get_vars()
        for key, val in new_vars.items():
            vars[key] = val

    def test_first(self):
        print("!!%s!!" % data_feeder.get_vars())
        pass
        # with apiritif.transaction('http://blazedemo.com/{}/{}'.format(vars['name'], vars['pass'])):
            # response = apiritif.http.get('http://blazedemo.com/{}/{}'.format(vars['name'], vars['pass']))

    def test_second(self):
        with open("/tmp/apiritif.log", "a") as _file:
            pid = str(os.getpid())
            tid = str(threading.current_thread().ident)
            hid = hashlib.md5()
            hid.update(pid.encode())
            hid.update(tid.encode())
            log_line = "%s. %s:%s {%s:%s}\n" % (hid.hexdigest()[:3], pid[-3:], tid[-3:], vars["name"], vars["pass"])
            print(log_line)
            _file.write(log_line)

