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
import shutil
from utils import shell


def validate(directory, force=False):
    if not os.path.exists(directory):
        os.mkdir(directory)

    if not os.path.isdir(directory):
        raise Exception("{} is not a directory".format(directory))

    if len(os.listdir(directory)) > 0:
        if not force:
            raise Exception("directory {} is not empty, use --force to truncate it".format(directory))
        shutil.rmtree(directory)
        os.mkdir(directory)


def write(directory, env, force=False):
    print_thread = shell.LoadingText("writing to directory {}".format(directory))
    print_thread.start()

    validate(directory, force)

    os.mkdir("{}/output".format(directory))

    env_file = os.open("{}/env.json".format(directory), os.O_WRONLY|os.O_CREAT|os.O_TRUNC)
    os.write(env_file, env.serialize().encode("utf-8"))
    os.close(env_file)

    for cmd in env.command_output:
        cmd_file = os.open("{}/output/{}".format(directory, cmd.friendly_name()), os.O_WRONLY|os.O_CREAT|os.O_TRUNC)
        os.write(cmd_file, cmd.output().encode("utf-8"))
        os.close(cmd_file)

    print_thread.shutdown_flag.set()
    print_thread.join()
