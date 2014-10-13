import unittest

from Game.Card.VictoryPoints.Test.suite import suite as victorypoints_suite
from Game.Card.Cost.Test.suite import suite as cost_suite

suites = [cost_suite,
          victorypoints_suite]
suite = unittest.TestSuite(suites)