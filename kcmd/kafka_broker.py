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


class KBrokerVersionCommand(command.KDiagCommand):
    def __init__(self, kafka_opts, listener):
        command.KDiagCommand.__init__(self, "bash", ["-c", "KAFKA_OPTS={} kafka-broker-api-versions --bootstrap-server localhost:{}".format(" ".join(kafka_opts), listener.split(":")[-1])])

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
