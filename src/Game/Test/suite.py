import unittest

from Game.Characters.Test.suite import suite as characters_suite
from Game.Card.Test.suite import suite as card_suite

suites = [card_suite,
          characters_suite]
suite = unittest.TestSuite(suites)