#!/usr/bin/env python
import os

from shlex import split

from utils import RunCMD
from constants import OS_TYPE, PORT_DIR


class Ports(object):
    __slots__ = ['port_name', 'port_options', '_run']

    def __init__(self, port_name, port_options):
        self.port_name = port_name
        self.port_options = port_options
        self._run = RunCMD()

    def compile_port(self, compile_options=None):
        port_path = None

        if not os.path.exists(PORT_DIR):
            [self._run(fetch) for fetch in facter.FETCH['PORTS']]

        try:
            for _dir, _, _ in os.walk(PORT_DIR):
                if "distfiles" in _dir:
                    continue

                if self.port_name in _dir:
                    port_path = PORT_DIR + split(str(_dir)[10:15])[0] + self.port_name

                    if not os.path.exists(port_path):
                        raise Die("No such port or port dir: %s %s" % (port_path, self.port_name))

                with cd(port_path):
                        self._run(facter.COMPILE['compile'] + compile_options)

        except Exception as Eerr:
                raise ("Error durin compiling {}: {}".format(self.port_name, Eerr))

    def pkg(self):



