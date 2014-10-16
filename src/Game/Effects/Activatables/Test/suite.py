import unittest

from Game.Effects.Activatables.Test.activatable_test import suite as activatable_suite

suites = [activatable_suite]
suite = unittest.TestSuite(suites)