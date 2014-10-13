import unittest

from Game.Card.Test.suite import suite as card_suite

suites = [card_suite]
suite = unittest.TestSuite(suites)