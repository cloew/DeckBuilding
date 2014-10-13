import unittest

from Game.Card.Test.card_test import suite as card_suite
from Game.Card.VictoryPoints.Test.suite import suite as victorypoints_suite
from Game.Card.Cost.Test.suite import suite as cost_suite

suites = [cost_suite,
          victorypoints_suite,
          card_suite]
suite = unittest.TestSuite(suites)