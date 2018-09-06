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
from model import mapper


class Serde(object):

    def serialize(self):
        return json.dumps(self.__dict__,
                          indent=4,
                          default=self.to_dict)

    def deserialize(self, kv):
        for attr, value in enumerate(kv):
            if not isinstance(value, {}):
                self.__dict__[attr] = value
            else:
                if attr in mapper.Mapper.mapping:
                    object_class = mapper.mapping()
                    obj = object_class()
                    obj.deserialize(value)
                    self.__dict__[attr] = obj
                else:
                    self.__dict__[attr] = value

        return self

    def to_dict(self, o):
        return o.__dict__
