import unittest

from Game.Decks.Test.deck_loader_test import suite as deck_loader_test_suite

suites = [deck_loader_test_suite]
suite = unittest.TestSuite(suites)