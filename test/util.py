# -*- coding: utf-8 -*-
"""Utilities to assist in testing."""

# import system modules
import inspect
import os
import sys
import unittest

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.split(MODULE_PATH)[0]
CONFIG = 'config.ini'
sys.path.append(BASE_PATH)

import configparser


def get_config():
    """Get the configuration for the test program."""
    config_path = os.path.join(MODULE_PATH, CONFIG)
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

class FSTemplateTest(unittest.TestCase):
    """FSTemplateTest is the base class for familysearch tests.
    """
    # common setup
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.config = get_config()
        self.devkey = self.config["fsTest"]["devkey"]
        self.username = self.config["fsTest"]["username"]
        self.username = self.config["fsTest"]["password"]

    # common teardown
    def tearDown(self):
        unittest.TestCase.tearDown(self)
