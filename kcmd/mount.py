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

class KMountCommand(command.KDiagCommand):
    def __init__(self, lfs):
        command.KDiagCommand.__init__(self, "cat", ["/etc/fstab"])
        lines = self._output.splitlines()
        self.mount_point = lfs
        self.fs = None
        self.fs_options = None

        for line in lines:
            line = str(line)

            if line == "":
                continue

            mount_point = line.split()

            if len(mount_point) <= 2:
                continue

            path = mount_point[1]

            if path == lfs:
                self.fs_options = self.parse_mount_options(mount_point[3])
                self.fs = mount_point[2]
                break

        self._env.kafka_log_mount_point = lfs
        self._env.kafka_log_mount_fs_options = self.fs_options
        self._env.kafka_log_mount_fs = self.fs

    def parse_mount_options(self, options):
        results = {}
        for opt in options.split(","):
            if "=" in opt:
                splitted = options.split("=")
                results[splitted[0]] = splitted[1].strip()
            else:
                results[opt] = None
        return results

