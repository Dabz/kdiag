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


class KReleaseCommand(command.KDiagCommand):
    lsb = {}

    def __init__(self):
        command.KDiagCommand.__init__(self, "lsb_release", ["-a"])
        lines = self._output.splitlines()

        for line in lines:
            splitted = line.split(":")
            name = splitted[0].strip()
            value = splitted[1].strip()
            self.lsb[name] = value

        self.linux_distribution = self.lsb["Distributor ID"]
        self.linux_distribution_version = self.lsb["Release"]
        self.linux_description = self.lsb["Description"]

        self._env.host_release = self.linux_distribution
        self._env.host_release_version = self.linux_distribution_version
        self._env.host_release_description = self.linux_description
