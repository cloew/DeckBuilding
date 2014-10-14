import unittest

from Game.Effects.Conditions.Filters.Operations.Test.operations_test import suite as operations_suite

suites = [operations_suite]
suite = unittest.TestSuite(suites)