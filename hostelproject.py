class Visitor:
    def __init__(self, name, visitor_id):
        self.name = name
        self.visitor_id = visitor_id

    def __str__(self):
        return f"{self.name} (ID: {self.visitor_id})"


class Resident:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"{self.name} [Room: {self.room}]"


class Hostel:
    def __init__(self, name):
        self.name = name
        self.visits = []   # list to store visits

    def record_visit(self, visitor, resident, arrival, departure):
        visit = {
            "visitor": visitor,
            "resident": resident,
            "arrival": arrival,
            "departure": departure
        }
        self.visits.append(visit)
        print(f"✅ Visit recorded: {visitor.name} visited {resident.name}")

    def show_visits(self):
        print(f"\n📋 Visit Records for {self.name}:")
        if not self.visits:
            print("No visits recorded yet.")
        else:
            for i, v in enumerate(self.visits, start=1):
                print(f"{i}. Visitor: {v['visitor']} → Resident: {v['resident']}, "
                      f"Arrival: {v['arrival']}, Departure: {v['departure']}")
# Create Visitor & Resident
visitor1 = Visitor("Ritah", "V5656")
resident1 = Resident("John", "102B")

# Create Hostel
hostel = Hostel("Alakara Hostel")

# Record Visit
hostel.record_visit(visitor1, resident1, "10:00 AM", "11:30 AM")

# Show Visits
hostel.show_visits()
