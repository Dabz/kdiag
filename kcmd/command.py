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
        self.succeed = True
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
        try:
            self._output = subprocess.check_output([self._cmd] + self._args).decode("utf-8")
        except subprocess.CalledProcessError:
            self.succeed = True
            print_thread.succeed = False

        command_name = self.__class__.__name__
        self._env.command_output.append(self)
        print_thread.shutdown_flag.set()
        print_thread.join()

    def friendly_name(self):
        if self._cmd == "bash":
            if len(self._args) > 1 and self._args[0] == "-c":
                return self._args[1].split()[0]
        return self._cmd

    def output(self):
        return self._output
