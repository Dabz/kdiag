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
from model import broker
from model import environment


class KBrokerVersionCommand(command.KDiagCommand):
    def __init__(self, kafka_opts, listener):
        self._env = environment.Environment.getInstance()
        security, hostname, port = self._env.listener()
        command.KDiagCommand.__init__(self, "bash", ["-c", "KAFKA_OPTS={} kafka-broker-api-versions "
                                                           "--bootstrap-server {}:{}".format(" ".join(kafka_opts),
                                                                                             hostname, port)])

        lines = self._output.splitlines()
        self.brokers = []

        for line in lines:
            if "-> (" not in line:
                continue

            brk = broker.KafkaBroker()
            brk.hostname = line.split(' (')[0]
            brk.id = line.split("id: ")[1].split(" rack")[0]
            brk.rack = line.split("rack: ")[1].split(")")[0]

            self.brokers.append(brk)

        self._env.kafka_brokers = self.brokers
