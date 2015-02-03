from Game.Commands.Requests.pick_up_to_n_card_request import PickUpToNCardRequest
from Game.Effects.pick_cards import PickCards

class PickUpToNCards(PickCards):
    """ Represents an effect to pick up to some number cards from a zone and an optional filter """
    REQUEST_CLASS = PickUpToNCardRequest
    AUTO_PICK = False