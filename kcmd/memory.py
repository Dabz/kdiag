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


class KMemoryCommand(command.KDiagCommand):
    def __init__(self):
        command.KDiagCommand.__init__(self, "free", [])
        lines = self._output.splitlines()
        memory_line = lines[1].split()
        swap_line = lines[2].split()

        self.memory_total = memory_line[1]
        self.memory_used = memory_line[2]
        self.memory_free = memory_line[3]
        self.memory_shared = memory_line[4]
        self.memory_buff = memory_line[5]
        self.memory_available = memory_line[6]

        self.swap_total = swap_line[1]
        self.swap_used = swap_line[2]
        self.swap_free = swap_line[3]

        self._env.host_memory_total = self.memory_total
        self._env.host_memory_used = self.memory_used
        self._env.host_memory_free = self.memory_free
        self._env.host_memory_shared = self.memory_shared
        self._env.host_memory_buff = self.memory_buff
        self._env.host_memory_available = self.memory_available

        self._env.host_swap_total = self.swap_total
        self._env.host_swap_used = self.swap_used
        self._env.host_swap_free = self.swap_free

