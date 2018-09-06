#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""

"""

import subprocess
import sys
import os
from model import environment
from utils import shell


class KDiagCommand:
    def __init__(self, lcmd, largs):
        self._cmd = lcmd
        self._args = largs
        self._env = environment.Environment.getInstance()
        self._output = None

        self.validate()
        self.execute()

    def validate(self):
        # Check if the command is available in the path
        with open(os.devnull, 'w') as FNULL:
            which_result = subprocess.call(["which", self._cmd], stdout=FNULL, stderr=subprocess.STDOUT)
            if which_result != 0:
                raise Exception("{} is not in the $PATH".format(self._cmd))

        return True

    def execute(self):
        print_thread = shell.LoadingText("executing `%s %s`" % (self._cmd, " ".join(self._args)))
        print_thread.start()
        self._output = subprocess.check_output([self._cmd] + self._args).decode("utf-8")
        command_name = self.__class__.__name__
        self._env.command_output[command_name] = self._output
        print_thread.shutdown_flag.set()
        print_thread.join()
