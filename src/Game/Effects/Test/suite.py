import unittest

from Game.Effects.Conditions.Test.suite import suite as conditions_suite

suites = [conditions_suite]
suite = unittest.TestSuite(suites)