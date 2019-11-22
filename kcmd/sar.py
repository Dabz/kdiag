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
from model import environment


class KSarCommand(command.KDiagCommand):
    lsb = {}

    def __init__(self):
        command.KDiagCommand.__init__(self, "sar", ["1", "15"])
        lines = self._output.splitlines()[2:]

        environment.Environment.getInstance().host_sar = []

        for line in lines:
            cpu = {}
            splitted = line.split()
            cpu["user"] = splitted[3]
            cpu["nice"] = splitted[4]
            cpu["system"] = splitted[5]
            cpu["iowait"] = splitted[6]
            cpu["steal"] = splitted[7]
            cpu["idle"] = splitted[-1]

            environment.Environment.getInstance().host_sar.append(cpu)
