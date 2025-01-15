 #TASK 1 Define the Applicant and Company Classes


class Applicant:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Company:
    def __init__(self, name, Software):
        self.name = name
        self.software = Software


#TASK 2 Create events:
class Event:
    def __init__(self, payload):
        self.payload = payload

class ApplicationSubmittedEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)

class ApplicationRejectedEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)

class ApplicationAcceptedEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)

#TASK 3 Create communication queue

from queue import Queue

class EventQueue:
    def __init__(self):
        self.queue = Queue()

    def add_event(self, event):
        self.queue.put(event)

    def process_events(self):
        while not self.queue.empty():
            event = self.queue.get()
            print(f"Processing {event.__class__.__name__} for {event.payload.name}")


#TASK 4 main py
def main():
    applicant = Applicant("Doga Simsek", "dogasimsek@gmail.com")
    company = Company("Doga Simsek", "Software")

    event_queue = EventQueue()

    event_queue.process_events()
    event_queue.add_event(ApplicationSubmittedEvent(applicant))
    event_queue.add_event(ApplicationRejectedEvent(applicant))
    event_queue.add_event(ApplicationAcceptedEvent(applicant))


    event_queue.process_events()





