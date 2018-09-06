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


class KCPUCommand(command.KDiagCommand):
    def __init__(self):
        command.KDiagCommand.__init__(self, "grep", ["-c", "^processor", "/proc/cpuinfo"])
        self.number_of_cores = self._output.strip()
        self._env.host_number_of_core = self.number_of_cores

