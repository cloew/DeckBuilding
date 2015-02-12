from kao_flask.kao_url import KaoURL

# Lobby Urls
startGameURL = KaoURL('/api/lobbies/<int:lobbyId>/start')
changeCharacterURL = KaoURL('/api/lobbies/<int:lobbyId>/player/<int:playerId>/changecharacter')
changeNameURL = KaoURL('/api/lobbies/<int:lobbyId>/player/<int:playerId>/changename')
changeDeckURL = KaoURL('/api/lobbies/<int:lobbyId>/player/<int:playerId>/changedeck')
changeNumberOfVillainsURL = KaoURL('/api/lobbies/<int:lobbyId>/player/<int:playerId>/changenumberofvillains')

# Game Card Action Urls
activateCardURL = KaoURL('/api/game/<int:gameId>/player/<int:playerId>/card/<int:cardId>/activate')
buyCardURL = KaoURL('/api/game/<int:gameId>/player/<int:playerId>/card/<int:cardId>/buy')
playCardURL = KaoURL('/api/game/<int:gameId>/player/<int:playerId>/card/<int:cardId>/play')