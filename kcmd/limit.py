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


class KLimitCommand(command.KDiagCommand):
    def __init__(self, pid):
        command.KDiagCommand.__init__(self, "cat", ["/proc/{}/limits".format(pid)])

        lines = self._output.splitlines()[1:]
        self.limits = {}

        for line in lines:
            splitted = line.split("  ")
            name = splitted[0]
            splitted = " ".join(splitted[1:]).split()
            self.limits[name] = min(float(splitted[0].replace('unlimited', 'inf')),
                                    float(splitted[1].replace('unlimited', 'inf')))

        self._env.kafka_limits = self.limits
