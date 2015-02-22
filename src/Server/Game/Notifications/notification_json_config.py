from kao_json import JsonConfig, JsonAttr, FieldAttr, KeywordAttr

from Game.Zones.zone import Zone

from Game.Notifications.cards_notification import CardsNotification
from Game.Notifications.movement_notification import MovementNotification
from Game.Notifications.notification import Notification
from Game.Notifications.reveal_notification import RevealNotification

def IsForYou(object, currentPlayer):
    """ Return if the notification is for the current player """
    return object.player is currentPlayer
    
def GetCards(notification, currentPlayer):
    """ Return the notification cards if they should be visible """
    if IsForYou(notification, currentPlayer) or not notification.private:
        return notification.cards
    else:
        return []

notificationConfig = [(Notification, [FieldAttr('type', field='notificationType'),
                                      JsonAttr('id', lambda notification, game: game.notificationTracker.indexOf(notification)+1, args=['game']),
                                      FieldAttr('name', field='player.name'),
                                      JsonAttr('isYou', IsForYou, args=['currentPlayer'])]),
                      JsonConfig(CardsNotification, [JsonAttr('cards', GetCards, args=['currentPlayer']),
                                                     FieldAttr('private'),
                                                     JsonAttr('count', lambda notification: len(notification.cards))]).inheritFrom(Notification),
                      JsonConfig(MovementNotification, [FieldAttr('from', field='fromZone'),
                                                        FieldAttr('to', field='toZone')]).inheritFrom(CardsNotification),
                      JsonConfig(RevealNotification, [FieldAttr('zone')]).inheritFrom(CardsNotification),
                      (Zone, [FieldAttr('zoneType', field='zoneType.name'),
                              FieldAttr('playerName', field='player.name'),
                              JsonAttr('isYou', IsForYou, args=['currentPlayer'])])
                      ]