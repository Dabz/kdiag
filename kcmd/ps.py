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


class KPSCommand(command.KDiagCommand):
    def __init__(self):
        command.KDiagCommand.__init__(self, "bash", ["-c", "ps -ef | grep -i '[^]]io.confluent.support.metrics.SupportedKafka'"])
        splited = self._output.split()
        if len(splited) <= 2:
            raise Exception("can not find a running Kafka broker locally")

        self.java_options = {}
        self.config = {}
        self.config_raw = ""
        self.pid = splited[1].strip()
        self.config_path = splited[-1].strip()
        self.parse_java_options(splited[6:])
        self.parse_config()

        self._env.kafka_jvm_options = self.java_options
        self._env.kafka_config = self.config
        self._env.kafka_pid = self.pid
        self._env.kafka_config_raw = self.config_raw

    def parse_java_options(self, options):
        for option in options:
            option = str(option)
            if not option.startswith("-"):
                continue

            option = option[1:]

            if option.startswith("Xmx"):
                self.java_options["Xmx"] = self.parse_jvm_memory(option[3:])
                continue

            if option.startswith("Xms"):
                self.java_options["Xms"] = self.parse_jvm_memory(option[3:])
                continue

            if ":" in option or "=" in option:
                splitted = option.replace("=", ":").split(":")
                name = splitted[0]
                value = ":".join(splitted[1:])
                self.java_options[name] = value
            else:
                self.java_options[option] = None

    def parse_config(self):
        with open(self.config_path) as f:
            for line in f:
                self.config_raw += line

                # this is a comment, ignoring this line
                if line.strip().startswith("#"):
                    continue

                # No idea what that is, but better skipping it
                if "=" not in line:
                    continue

                splited = line.split("=")
                self.config[splited[0].strip()] = "=".join(splited[1:]).strip()

    def parse_jvm_memory(self, memory):
        digits, suffix = memory[:-1], memory[-1].upper()
        increment = 1

        if suffix == "K":
            increment = 1024 * 1024
        if suffix == "M":
            increment = 1024 * 1024
        if suffix == "G":
            increment = 1024 * 1024 * 1024

        return int(digits) * increment

