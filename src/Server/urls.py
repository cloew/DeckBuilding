from kao_flask.kao_url import KaoURL

activateCardURL = KaoURL('/api/game/<int:gameId>/player/<int:playerId>/card/<int:cardId>/activate')
buyCardURL = KaoURL('/api/game/<int:gameId>/player/<int:playerId>/card/<int:cardId>/buy')
playCardURL = KaoURL('/api/game/<int:gameId>/player/<int:playerId>/card/<int:cardId>/play')