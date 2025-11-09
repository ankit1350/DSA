class EventSystem:
    def __init__(self):
        self.event_queue = []  # Using list as queue (FIFO)

    # ✨ Add New Event
    def add_event(self, event):
        self.event_queue.append(event)  # Add at the end
        print("Event added successfully!")

    # ✨ Process Next Event (FIFO)
    def process_event(self):
        if not self.event_queue:
            print("No events to process!")
        else:
            event = self.event_queue.pop(0)  # Remove first event
            print(f"Processing Event: {event}")

    # ✨ Display Pending Events
    def display_events(self):
        if not self.event_queue:
            print("No pending events!")
        else:
            print("\nPending Events in Queue:")
            for i, event in enumerate(self.event_queue, start=1):
                print(f"{i}. {event}")

    # ✨ Cancel an Event (only if not yet processed)
    def cancel_event(self, event):
        if event in self.event_queue:
            self.event_queue.remove(event)
            print(f"Event '{event}' canceled successfully!")
        else:
            print("Event not found or already processed!")


# ✅ Main menu-driven program
system = EventSystem()

while True:
    print("\n--- REAL-TIME EVENT PROCESSING SYSTEM ---")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        event_name = input("Enter event name: ")
        system.add_event(event_name)

    elif choice == "2":
        system.process_event()

    elif choice == "3":
        system.display_events()

    elif choice == "4":
        cancel_name = input("Enter event name to cancel: ")
        system.cancel_event(cancel_name)

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice! Try again.")
