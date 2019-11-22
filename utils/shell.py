#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""
"""

import itertools
import threading
import time
import sys


class LoadingText(threading.Thread):

    def __init__(self, ltext):
        threading.Thread.__init__(self)
        self.text = ltext.strip()
        self.shutdown_flag = threading.Event()
        self.setDaemon(True)
        self.succeed = True

    def run(self):
        iteration = 0
        while not self.shutdown_flag.is_set():
            sys.stdout.write('\r☐  - {} {}    \r'.format(self.text, '.' * (iteration % 4)))
            sys.stdout.flush()
            iteration += 1
            time.sleep(0.3)

        if self.succeed:
            sys.stdout.write('\r☑  - {}\n'.format(self.text))
        else:
            sys.stdout.write('\r☑  - {}\n'.format(self.text))
