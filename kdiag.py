#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""
Utility to gather as much information as possible from your 
Kafka environment.
It has been designed to avoid round-trip between multiple teams,
e.g. between support and an application team, by gathergin all
required information. 
"""

from kcmd import (
    ps, mount, df, limit, swappiness, release, thp,
    memory, cpu, kafka_describe, kafka_broker, lsblk,
    sar, kafka_version, jmx
)

from tests import (
     limitoffiles
)

from model import environment

from utils import shell, writer, reader

import argparse
import sys
import tempfile


def display():
    pass


def test():
    limitoffiles.LimitOfFiles().execute()


def gather():
    env = environment.Environment.getInstance()

    kafka_version.KKafkaVersionCommand()
    ps.KPSCommand()
    cpu.KCPUCommand()
    memory.KMemoryCommand()
    lsblk.KLsblkCommand()
    df.KDfCommand(env.kafka_config['log.dirs'])
    mount.KMountCommand(env.kafka_log_mounted_on)
    limit.KLimitCommand(env.kafka_pid)
    swappiness.KSwappinessCommand()
    release.KReleaseCommand()
    thp.KTransparentHugePageCommand()
    sar.KSarCommand()
    jmx.KJMXCommand()

    security_enabled = "Djava.security.auth.login.config" in env.kafka_jvm_options
    jvm_options = []

    if security_enabled:
        jvm_options.append("-Djava.security.auth.login.config=%s"
                           % (env.kafka_jvm_options["Djava.security.auth.login.config"]))

    kafka_describe.KDescribeCommand(jvm_options, env.kafka_config["zookeeper.connect"])
    kafka_broker.KBrokerVersionCommand(jvm_options, env.kafka_config.get('listeners', 'localhost:9092'))


def main():
    parser = argparse.ArgumentParser(description='Gather information about the Apache Kafka host.')
    parser.add_argument('command', nargs='?',
                        default="gather", choices=["gather", "display", "test"],
                        help='command to perform, either gather (default), analyze or display')

    parser.add_argument('--directory',
                        help='input or output directory')

    parser.add_argument('--force', '-f', nargs="?",
                        const=True, default=False, type=bool,
                        help='force the output even if the directory contains data')

    ns = parser.parse_args(sys.argv[1:])

    if ns.command == "gather":
        directory = ns.directory
        if directory is None:
            directory = tempfile.mkdtemp('_output', 'kdiag_')

        writer.validate(directory, force=ns.force)
        gather()
        sys.stdout.write("\n")
        writer.write(directory, environment.Environment.getInstance(), force=ns.force)
    elif ns.command == "display":
        directory = ns.directory
        if directory is None:
            raise Exception("require input directory to be specified")
        display(directory)
    elif ns.command == "test":
        directory = ns.directory
        if directory is None:
            raise Exception("require input directory to be specified")

        reader.read(directory)
        test()

        pass


if __name__ == "__main__":
    main()

