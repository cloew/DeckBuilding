import unittest

from Game.Effects.Triggers.Test.trigger_test import suite as trigger_suite

suites = [trigger_suite]
suite = unittest.TestSuite(suites)