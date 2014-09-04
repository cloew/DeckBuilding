from Game.Card.card import Card
from Game.Effects.gain_power import GainPower

from kao_deck.deck_initializer import DeckInitializer

vulnerability = Card("Vulnerability")
punch = Card("Punch", playEffects=[GainPower(1)])

StartingDeckInitializer = DeckInitializer()
StartingDeckInitializer.addSameItem(vulnerability, 3)
StartingDeckInitializer.addSameItem(punch, 7)