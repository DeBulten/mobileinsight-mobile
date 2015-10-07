# -*- coding: utf-8 -*-
import urllib
import os
import platform
import sys
import platform
import stat
from distutils.core import setup, Extension

dm_collector_c_module = Extension('mobile_insight.monitor.dm_collector.dm_collector_c',
                                sources = [ "dm_collector_c/dm_collector_c.cpp",
                                            "dm_collector_c/hdlc.cpp",
                                            "dm_collector_c/log_config.cpp",
                                            "dm_collector_c/log_packet.cpp",
                                            "dm_collector_c/utils.cpp",])

setup(
    name = 'MobileInsight',
    version = '1.0',
    description = 'Mobile network monitoring and analysis',
    author = 'Yuanjie Li, Jiayao Li',
    author_email = 'yuanjie.li@cs.ucla.edu, likayo@ucla.edu',
    url = 'http://metro.cs.ucla.edu/mobile_insight',
    license = 'Apache License 2.0',
    packages = ['mobile_insight',
                'mobile_insight.analyzer',
                'mobile_insight.monitor',
                'mobile_insight.monitor.dm_collector',
                'mobile_insight.monitor.dm_collector.dm_endec',
                ],
    ext_modules = [dm_collector_c_module],
)