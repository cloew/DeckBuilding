import unittest

from Game.Card.Cost.Test.fixed_cost_test import suite as fixed_cost_suite

suites = [fixed_cost_suite]
suite = unittest.TestSuite(suites)