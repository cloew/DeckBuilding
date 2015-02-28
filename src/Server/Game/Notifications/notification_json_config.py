from kao_json import JsonConfig, JsonAttr, FieldAttr, KeywordAttr

from Game.Zones.zone import Zone

from Game.Notifications.cards_notification import CardsNotification
from Game.Notifications.movement_notification import MovementNotification
from Game.Notifications.notification import Notification
from Game.Notifications.reveal_notification import RevealNotification

def GetPlayer(notification):
    """ Return if the notification is for the current player """
    if notification.player:
        return {'name':notification.player.name}
    else:
        return None
    
def IsForYou(notification, currentPlayer):
    """ Return if the notification is for the current player """
    return notification.player is currentPlayer
    
def GetCards(notification, currentPlayer):
    """ Return the notification cards if they should be visible """
    if IsForYou(notification, currentPlayer) or not notification.private:
        return notification.cards
    else:
        return []

notificationConfig = [(Notification, [FieldAttr('type', field='notificationType'),
                                      FieldAttr('id'),
                                      JsonAttr('player', GetPlayer),
                                      JsonAttr('isYou', IsForYou, args=['currentPlayer']),
                                      FieldAttr('notifications')]),
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