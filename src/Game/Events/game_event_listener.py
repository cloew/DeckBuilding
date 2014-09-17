
class GameEventListener:
    """ Listener that monitors Game Events """
    
    def __init__(self):
        """ Initialize the Game Event Listener """
        self.observers = {}
        
    def registerTriggers(self, triggers):
        """ Register the triggers """
        for trigger in triggers:
            self.register(trigger.subject, trigger)
            
    def unregisterTriggers(self, triggers):
        """ Unregister the triggers """
        for trigger in triggers:
            self.unregister(trigger.subject, trigger)
        
    def register(self, subject, observer):
        """ Register an observer to the given subject """
        if subject not in self.observers:
            self.observers[subject] = []
        self.observers[subject].append(observer)
        
    def unregister(self, subject, observer):
        """ Unregister an observer from the given subject """
        if subject in self.observers:
            self.observers[subject].remove(observer)
        
    def send(self, event):
        """ Send the event signal to each observer """
        if event.subject in self.observers:
            for observer in self.observers[event.subject]:
                try:
                    coroutine = observer.receive(event)
                    response = yield coroutine.next()
                    while True:
                        response = yield coroutine.send(response)
                except StopIteration:
                    pass