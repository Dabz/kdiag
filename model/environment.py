#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""

"""

import json
from model import serde


class Environment(serde.Serde):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Environment.__instance is None:
            Environment()
        return Environment.__instance

    def __init__(self):
        Environment.__instance = self

        self.kafka_jvm_options = None
        self.kafka_config = None
        self.kafka_config_raw = None
        self.kafka_pid = None
        self.kafka_log_path = None
        self.kafka_log_mount_point = None
        self.kafka_log_mount_fs = None
        self.kafka_log_mount_fs_options = None
        self.kafka_log_mount_size = None
        self.kafka_log_mount_used = None
        self.kafka_log_mount_available = None
        self.kafka_log_mount_used_percentage = None
        self.kafka_log_mounted_on = None
        self.kafka_limits = None

        self.host_release = None
        self.host_release_version = None
        self.host_release_description = None

        self.host_number_of_core = None
        self.host_memory_total = None
        self.host_memory_used = None
        self.host_memory_free = None
        self.host_memory_shared = None
        self.host_memory_buff = None
        self.host_memory_available = None
        self.host_swap_total = None
        self.host_swap_used = None
        self.host_swap_free = None
        self.host_swappiness = None
        self.host_transparent_huge_page = None

        self.kafka_topics = None
        self.kafka_brokers = None

        self.command_output = {}

