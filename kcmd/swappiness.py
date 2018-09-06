#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""

"""

from kcmd import command


class KSwappinessCommand(command.KDiagCommand):
    def __init__(self):
        command.KDiagCommand.__init__(self, "cat", ["/proc/sys/vm/swappiness"])
        self.swappiness = self._output
        self._env.host_swappiness = self.swappiness
