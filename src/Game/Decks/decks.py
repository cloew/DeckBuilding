from Game.Card.card import Card
from Game.Card.Cost.fixed_cost import FixedCost

from Game.Effects.draw import Draw
from Game.Effects.gain_power import GainPower

from kao_deck.deck_initializer import DeckInitializer

vulnerability = Card("Vulnerability", costCalculator=FixedCost(0))
punch = Card("Punch", costCalculator=FixedCost(0), playEffects=[GainPower(1)])
kidFlash = Card("Kid Flash", costCalculator=FixedCost(2), playEffects=[Draw(count=1)])

StartingDeckInitializer = DeckInitializer()
StartingDeckInitializer.addItem(vulnerability, count=3)
StartingDeckInitializer.addItem(punch, count=7)

MainDeckInitializer = DeckInitializer()
MainDeckInitializer.addItem(kidFlash, count=20)