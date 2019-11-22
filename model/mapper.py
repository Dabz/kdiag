#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""

"""


def mapping():
    from model import topic, broker
    return {
        "kafka_topics": topic.KafkaTopic,
        "kafka_brokers": broker.KafkaBroker
    }

