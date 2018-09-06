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


class KTransparentHugePageCommand(command.KDiagCommand):
    def __init__(self):
        command.KDiagCommand.__init__(self, "cat", ["/sys/kernel/mm/transparent_hugepage/enabled"])
        splitted = self._output.split()

        # output it of the following format
        #    always [madvise] never
        # the option surrounded by bracket is the active one

        for option in splitted:
            if option.startswith("[") and option.endswith("]"):
                self.transparent_huge_page = option[1:-1]
                break

        self._env.host_transparent_huge_page = self.transparent_huge_page
