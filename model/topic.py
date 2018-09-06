#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""

"""

from model import serde


class KafkaPartition(serde.Serde):
    leader = 0
    isr = []
    replicas = []
    partition = 0

    @staticmethod
    def parse_describe_line(line):
        partition = KafkaPartition()

        # Easier to parse and split by removing space
        # this to avoid `Leader: 0`
        line = line.replace(": ", ":")
        splitted = line.split()
        local_config = {}

        for option in splitted:
            split_by_colon = option.split(":")
            name = split_by_colon[0]
            value = split_by_colon[1]
            local_config[name] = value

        partition.leader = local_config["Leader"]
        partition.isr = local_config["Isr"].split(",")
        partition.isr = local_config["Replicas"].split(",")
        partition.partition = local_config["Partition"]

        return partition


class KafkaTopic(serde.Serde):
    name = ""
    replication_factor = 0
    partitions = 0
    config = {}
    partitions = []

    @staticmethod
    def is_header_line(line):
        if not line.startswith("Topic:"):
            return False

        if "Configs" not in line:
            return False

        return True

    @staticmethod
    def parse_describe_line(line):
        line = str(line)
        topic = KafkaTopic()
        splitted = line.split()
        local_config = {}
        topic.partitions = []

        for option in splitted:
            split_by_colon = option.split(":")
            name = split_by_colon[0]
            value = split_by_colon[1]
            local_config[name] = value.strip()

        topic.replicas = local_config["ReplicationFactor"]
        topic.partition_count = local_config["PartitionCount"]
        topic.name = local_config["Topic"]
        topic.config = {}
        split_options = local_config["Configs"].split(",")

        for option in split_options:
            split_by_colon = option.split("=")

            if len(split_by_colon) < 2:
                continue

            name = split_by_colon[0]
            value = split_by_colon[1]

            topic.config[name] = value

        return topic
