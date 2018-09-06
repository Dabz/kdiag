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


class KLsblkCommand(command.KDiagCommand):
    def __init__(self):
        command.KDiagCommand.__init__(self, "lsblk", [])
        self.lsblk = self._output
