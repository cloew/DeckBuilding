from Game.Card.card import Card
from Game.Effects.draw import Draw
from Game.Effects.gain_power import GainPower

from kao_deck.deck_initializer import DeckInitializer

vulnerability = Card("Vulnerability")
punch = Card("Punch", playEffects=[GainPower(1)])
kidFlash = Card("Kid Flash", playEffects=[Draw(count=1)])

StartingDeckInitializer = DeckInitializer()
StartingDeckInitializer.addItem(vulnerability, count=3)
StartingDeckInitializer.addItem(punch, count=7)

MainDeckInitializer = DeckInitializer()
MainDeckInitializer.addItem(kidFlash, count=20)