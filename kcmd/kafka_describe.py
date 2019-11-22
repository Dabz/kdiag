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
from model import topic

class KDescribeCommand(command.KDiagCommand):
    def __init__(self, kafka_opts, zookeeper):
        command.KDiagCommand.__init__(self, "bash", ["-c", "KAFKA_OPTS={} kafka-topics --zookeeper {} --describe".format(" ".join(kafka_opts), zookeeper)])

        self.topics = []
        lines = self._output.splitlines()
        for line in lines:
            if topic.KafkaTopic.is_header_line(line):
                self.topics.append(topic.KafkaTopic.parse_describe_line(line))
            else:
                self.topics[-1].partitions.append(topic.KafkaPartition.parse_describe_line(line))

        self._env.kafka_topics = self.topics
