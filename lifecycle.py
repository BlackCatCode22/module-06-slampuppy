class PartyAnimal:

    def __init__(self):
        self.x = 0
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

    def __del__(self):
        print("I am destructed", self.x)


s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")
j.party()
