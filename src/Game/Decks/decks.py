from Game.Card.card import Card
from Game.Card.card_factory import CardFactory
from Game.Card.Cost.fixed_cost import FixedCost

from Game.Effects.draw import Draw
from Game.Effects.gain_power import GainPower

from kao_deck.deck_initializer import DeckInitializer

vulnerability = CardFactory.loadCard("Vulnerability") # Card("Vulnerability", costCalculator=FixedCost(0))
punch = CardFactory.loadCard("Punch") #Card("Punch", costCalculator=FixedCost(0), playEffects=[GainPower(1)])
kick = Card("Kick", costCalculator=FixedCost(3), playEffects=[GainPower(2)])
kidFlash = Card("Kid Flash", costCalculator=FixedCost(2), playEffects=[Draw(count=1)])

StartingDeckInitializer = DeckInitializer()
StartingDeckInitializer.addItem(vulnerability, count=2)
StartingDeckInitializer.addItem(punch, count=8)

KickDeckInitializer = DeckInitializer()
KickDeckInitializer.addItem(kick, count=30)

MainDeckInitializer = DeckInitializer()
MainDeckInitializer.addItem(kidFlash, count=20)