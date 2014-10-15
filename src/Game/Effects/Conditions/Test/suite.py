import unittest

from Game.Effects.Conditions.Test.not_condition_test import suite as not_condition_suite
from Game.Effects.Conditions.Test.matching_test import suite as matching_suite
from Game.Effects.Conditions.Test.is_player_turn_test import suite as is_player_turn_suite
from Game.Effects.Conditions.Test.has_cards_test import suite as has_cards_suite
from Game.Effects.Conditions.Test.full_line_up_test import suite as full_line_up_suite
from Game.Effects.Conditions.Test.enough_power_test import suite as enough_power_suite
from Game.Effects.Conditions.Test.and_condition_test import suite as and_condition_suite
from Game.Effects.Conditions.Filters.Test.suite import suite as filters_suite

suites = [filters_suite,
          and_condition_suite,
          enough_power_suite,
          full_line_up_suite,
          has_cards_suite,
          is_player_turn_suite,
          matching_suite,
          not_condition_suite]
suite = unittest.TestSuite(suites)