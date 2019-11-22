#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""

"""
from abc import abstractmethod

from model import environment
from utils import shell
import subprocess


class TestException(Exception):
    message = ""

    def __init__(self, message):
        self.message = message


class Test:
    def __init__(self):
        self._env = environment.Environment.getInstance()
        self.name = "test"
        self.message = ""

    @abstractmethod
    def execute_test(self):
        return "TODO: implement me"

    def execute(self):
        print_thread = shell.LoadingText("executing test `%s`" % self.name)
        print_thread.start()
        self.message = self.execute_test()
        print_thread.succeed = self.succeed()
        print_thread.additional_message = self.message
        print_thread.shutdown_flag.set()
        print_thread.join()

    def succeed(self):
        if self.message:
            return False
        else:
            return True
