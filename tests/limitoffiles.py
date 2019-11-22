#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""

"""
from tests import test


class LimitOfFiles(test.Test):
    def __init__(self):
        test.Test.__init__(self)
        self.name = "file limit"

    def execute_test(self):
        limitNoFiles = int(self._env.kafka_limits["Max open files"])

        if limitNoFiles <= 1000000:
            return "LimitsNOFiles should be set to a value greater than 100,000"

        return None
