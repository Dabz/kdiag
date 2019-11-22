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
from model import environment


class KJMXCommand(command.KDiagCommand):

    metrics_to_gather = [
        "kafka.controller:type=KafkaController,name=OfflinePartitionsCount",
        "kafka.server:type=ReplicaManager,name=UnderMinIsrPartitionCount",
        "kafka.server:type=ReplicaManager,name=UnderReplicatedPartitions",
        "kafka.server:type=KafkaRequestHandlerPool,name=RequestHandlerAvgIdlePercent",
        "kafka.network:type=SocketServer,name=NetworkProcessorAvgIdlePercent"
    ]

    def __init__(self):
        self._env = environment.Environment.getInstance()
        if self._env.kafka_jmx_enabled:
            command.KDiagCommand.__init__(self, "bash", ["-c", self.format_command()])
        else:
            command.KDiagCommand.__init__(self, "bash", ["-c", "echo JMX not enabled on Kafka && exit 1"])

        if not self.succeed:
            return

        splited = self._output.split("\n")
        kafka_jms_metrics = {}

        for line in splited[1:]:
            if not line:
                continue
            line_splited = line.split("\t")
            metric_name = line_splited[0]
            value = line_splited[1]
            kafka_jms_metrics[metric_name] = value

        self._env.kafka_jmx_metrics = kafka_jms_metrics

    def format_command(self):
        attributes = ""
        for attr in self.metrics_to_gather:
            attributes += " --object-name '%s' " % attr;

        return "kafka-run-class kafka.tools.JmxTool --one-time true --report-format tsv " \
               "--jmx-url 'service:jmx:rmi:///jndi/rmi://:%s/jmxrmi' %s" % (self._env.kafka_jmx_port, attributes)
