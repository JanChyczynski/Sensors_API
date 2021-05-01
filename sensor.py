class Sensor:
    def __init__(self, address=None, owner=None):
        self.address = address
        self.owner = owner

    def __dict__(self):
        return {"address": self.address, "owner": self.owner}