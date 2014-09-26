# from Game.Card.card import Card
# from Game.Card.card_factory import CardFactory
# from Game.Card.Cost.fixed_cost import FixedCost

from Game.Decks.deck_factory import DeckFactory

# from Game.Effects.draw import Draw
# from Game.Effects.gain_power import GainPower

# from kao_deck.deck_initializer import DeckInitializer

# vulnerability = CardFactory.loadCard("Vulnerability")
# punch = CardFactory.loadCard("Punch")
# kick = CardFactory.loadCard("Kick")
# kidFlash = CardFactory.loadCard("Kid Flash")

StartingDeckInitializer = DeckFactory.loadDeck("Starting")
# StartingDeckInitializer.addItem(kidFlash, count=3)
# StartingDeckInitializer.addItem(punch, count=7)

KickDeckInitializer = DeckFactory.loadDeck("Kick")
# KickDeckInitializer.addItem(kick, count=30)

MainDeckInitializer = DeckFactory.loadDeck("Deck 1")
# MainDeckInitializer.addItem(kidFlash, count=20)

SuperVillainDeckInitializer = DeckFactory.loadDeck("Super Villains")