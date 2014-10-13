import unittest

from Game.Characters.Test.character_test import suite as character_suite

suites = [character_suite]
suite = unittest.TestSuite(suites)