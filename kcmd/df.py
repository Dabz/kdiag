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


class KDfCommand(command.KDiagCommand):
    def __init__(self, lfs):
        command.KDiagCommand.__init__(self, "df", ["-h", lfs])
        lines = self._output.splitlines()
        mount_point = lines[1].split()
        self.mount_size = mount_point[1].strip()
        self.mount_used = mount_point[2].strip()
        self.mount_available = mount_point[3].strip()
        self.mount_used_percentage = mount_point[4].strip()
        self.mounted_on = mount_point[5].strip()

        self._env.kafka_log_mounted_on = self.mounted_on
        self._env.kafka_log_mount_size = self.mount_size
        self._env.kafka_log_mount_available = self.mount_available
        self._env.kafka_log_mount_used_percentage = self.mount_used_percentage
        self._env.kafka_log_mount_used = self.mount_used
