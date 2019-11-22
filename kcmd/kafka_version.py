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


class KKafkaVersionCommand(command.KDiagCommand):
    def __init__(self):
        command.KDiagCommand.__init__(self, "kafka-topics", ["--version"])

        lines = self._output.splitlines()
        self._env.kafka_version = lines[0]
        self._env.kafka_major_version = lines[0].split(".")[0]
