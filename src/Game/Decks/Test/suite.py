import unittest

from Game.Decks.Test.fixed_top_card_deck_loader_test import suite as fixed_top_card_deck_loader_suite
from Game.Decks.Test.starting_deck_loader_test import suite as starting_deck_loader_suite
from Game.Decks.Test.shuffling_deck_loader_test import suite as shuffling_deck_loader_suite
from Game.Decks.Test.deck_loader_test import suite as deck_loader_test_suite

suites = [deck_loader_test_suite,
          shuffling_deck_loader_suite,
          starting_deck_loader_suite,
          fixed_top_card_deck_loader_suite]
suite = unittest.TestSuite(suites)