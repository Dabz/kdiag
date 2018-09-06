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

class KafkaBroker(serde.Serde):
    hostname = None
    rack = None
    id = None

    def __init__(self):
        pass

