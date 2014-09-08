
class GameEventListener:
    """ Listener that monitors Game Events """
    
    def __init__(self):
        """ Initialize the Game Event Listener """
        self.observers = {}
        
    def register(self, subject, observer):
        """ Register an observer to the given subject """
        if subject not  in self.observers:
            self.observers[subject] = []
        self.observers[subject].append(observer)
        
    def send(self, event):
        """ Send the event signal to each observer """
        if event.subject in self.observers:
            for observer in self.observers[event.subject]:
                observer.respond(event)