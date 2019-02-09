
class LeaderBoard:
    def __init__(self,name,disc):
        self.name = name
        self.display = disc

class Mg(LeaderBoard):
    def run(self):
        print("mani is running")

abcd = Mg("Mnai","Kanta")
print(abcd.name)
abcd.run()