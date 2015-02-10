from kao_json import JsonConfig, JsonAttr, FieldAttr, KeywordAttr

from Game.Notifications.cards_notification import CardsNotification
from Game.Notifications.notification import Notification
from Game.Notifications.reveal_notification import RevealNotification

notificationConfig = [(Notification, [FieldAttr('type', field='notificationType'),
                                      JsonAttr('id', lambda notification, game: game.notificationTracker.indexOf(notification)+1, args=['game']),
                                      FieldAttr('name', field='player.name'),
                                      JsonAttr('isYou', lambda notification, currentPlayer: notification.player is currentPlayer, args=['currentPlayer'])],
                      JsonConfig(CardsNotification, [FieldAttr('cards')]).inheritFrom(Notification),
                      JsonConfig(RevealNotification, [FieldAttr('zoneType')]).inheritFrom(CardsNotification)
                      )]