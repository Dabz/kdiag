#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaspar_d </var/spool/mail/gaspar_d>
#
# Distributed under terms of the MIT license.

"""
"""

import os
import json
from utils import shell
from model import environment


def validate(directory, force=False):
    if not os.path.exists(directory):
        os.mkdir(directory)

    if not os.path.isdir(directory):
        raise Exception("{} is not a directory".format(directory))


def read(directory):
    print_thread = shell.LoadingText("reading from directory {}".format(directory))
    print_thread.start()

    validate(directory, False)

    with open("{}/env.json".format(directory), "r") as env_file:
        env_json_string = env_file.read()
        env_json = json.loads(env_json_string)
        environment.Environment.getInstance().deserialize(env_json)

    print_thread.shutdown_flag.set()
    print_thread.join()
